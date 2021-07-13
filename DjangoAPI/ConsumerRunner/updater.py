
from datetime import datetime
import ConsumerRunner
from apscheduler.schedulers.background import BackgroundScheduler
from ConsumerRunner import consumer, producer

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(consumer.cons, 'interval', seconds =2)
   # scheduler.add_job(producer.kfk, 'interval', seconds =1)
    scheduler.start()