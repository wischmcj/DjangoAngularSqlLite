
from kafka import KafkaProducer
from django.http import HttpResponse
import pickle

def kfk():  
    print("produce") 
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    v = {
        'msg': {
            'I am': 'Jeff',
        },
    }
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    producer.send('Ptopic', serialized_data)
    return HttpResponse(200)

def main():
    kfk()

if __name__ == '__main__':
    main()