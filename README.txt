To run the Django api you have to start my
Env (the python environment) first
Got to ../scripts and run 'activate'

You can then navigate to ../DjangoAPI and run the typical 'python manage.py runserver' command


Commands to run Kafka

C:\Users\wisch\kafka\kafka_2.13-2.6.0

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

.\bin\windows\kafka-server-start.bat .\config\server.properties

To activate env and nav to app

activate 
cd ..
cd ..
cd DjangoApi

python manage.py runserver --noreload