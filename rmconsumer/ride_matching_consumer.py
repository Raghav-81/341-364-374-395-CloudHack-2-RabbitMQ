# Code for Ride Matching Consumer
import pika
import os

import json
import requests

import time

time.sleep(60)

# consumerIP address = "192.168.1.1", name = "consumer1"


consumerIP = os.environ['CONSUMERIP']
consumerID = os.environ['CUST_ID']
name = os.environ['CONSUMERNAME']
consumerdict2 = {'consumerIP' : consumerIP, 'consumerID' : consumerID, 'name' : name}


def main():   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue = 'ridematch')  

    #This function is to serve the consumer
    def callback(ch, method, properties, body):
        ride = json.loads(body.decode('utf-8'))
        sleeptime = ride['time']
        time.sleep(int(sleeptime))
        print("Consumer - " + consumerID)
        print(" Ride served - ", ride)

    postreq = requests.post('http://producer:6000/new_ride_matching_consumer', json = consumerdict2)
    print("definitely came till hereeee")
    channel.basic_consume(queue = 'ridematch', on_message_callback = callback, auto_ack = True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()