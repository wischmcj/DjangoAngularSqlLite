from EmployeeApp.models import Departments,Employees
import sqlite3
from sqlite3 import Error
import pickle
from django.http import HttpRequest,HttpResponse
from celery import shared_task

from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from .constants import USER_SCHEMA, USER_TOPIC
from .transformers import dict_to_user
import logging
import traceback
import logging
import traceback

# Kafka

@shared_task
def cons(request):
    json_deserializer = JSONDeserializer(USER_SCHEMA, from_dict=dict_to_user)
    string_deserializer = StringDeserializer('utf_8')
    consumer_conf = {'bootstrap.servers': 'localhost:9092',
                     'key.deserializer': string_deserializer,
                     'value.deserializer': json_deserializer,
                     'group.id': 'django-kafka',
                     'auto.offset.reset': "earliest"}
    
    consumer = DeserializingConsumer(consumer_conf)
    consumer.subscribe([USER_TOPIC])

    print('serialized_data' )
    print('consumer' )
    
    """
    The idea is to start the Kafka consumer when the message is sent to the Kafka producer.
    Resulting in two queues: Task Queue and Message/Content Queue.
    Multi-threading might be an overkill for a simple application, hence the for loop (Temporary). 
    """
    for x in range(200):
        try:
            msg = consumer.poll(timeout=5.0)
            if msg is not None:
                user = msg.value()
                if user is not None:
                    print("User record {}: username: {}\n"
                          "\tdata: {}\n"
                          .format(msg.key(), user.username,
                                  user.data))

        except Exception as e:
            print('An exception occurred: {}'.format(e))
            logging.error(traceback.format_exc())

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
    
def create_dept(conn, department):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO EmployeeApp_departments(DepartmentName)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, department)
    conn.commit()
    return cur.lastrowid

# def main():
#     database = r"C:\Users\wisch\OneDrive\Documents\GItHubProjects\PersonalProjects\DjangoAngularSqlLite\DjangoAPI\db.sqlite3"

#     # create a database connection
#     conn = create_connection(database)
#     with conn:
#         # create a new project
#         for message in consumer:
#             deserialized_data = pickle.loads(message.value) 
#             print(deserialized_data)
#         department = ('TestDepartment');
#         DepartmentID = create_emp(conn, department)
#         logging.warning(DepartmentID)

