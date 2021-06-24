
import json

from EmployeeApp.models import Departments,Employees
from kafka import KafkaConsumer,KafkaProducer,TopicPartition
import threading, time
from datetime import datetime
from math import sqrt
import statistics
import sqlite3
from sqlite3 import Error
import logging
from kafka import KafkaConsumer
import _sqlite3

def calculate_standard_deviation(user_id):
	x = [i.amount for i in Transaction.objects(user=user_id).only('amount')]
	try:
		return statistics.stdev(x)
	except:
		return float('inf')


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

def create_emp(conn, employee):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO EmployeeApp_departments(DepartmentID,DepartmentName)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid
    

def main():
    database = r"C:\Users\wisch\OneDrive\Documents\GItHubProjects\PersonalProjects\DjangoAngularSqlLite\DjangoAPI\db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        employee = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        employee_id = create_emp(conn, employee)
        logging.warning(employee_id)


if __name__ == '__main__':
    main()