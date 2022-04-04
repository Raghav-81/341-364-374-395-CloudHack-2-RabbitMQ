# Code for Producer
import pika

import json
from flask import Flask, request


app = Flask(__name__)

app.secret_key = "cchackathon2"
	
@app.route('/')

def index():
	return "Server is running"

@app.route('/new_ride', methods = ['POST'])
def newride():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel2 = connection.channel()
    channel.queue_declare(queue = 'ridematch')
    channel2.queue_declare(queue = 'database')
    ridedetails = {}
    ridedetails['pickup'] = request.form['pickup']
    ridedetails['destination'] = request.form['destination']
    ridedetails['time'] = request.form['time']
    ridedetails['cost'] = request.form['cost']
    ridedetails['seats'] = request.form['seats']
    channel.basic_publish(exchange = '', routing_key = 'ridematch', body = json.dumps(ridedetails))
    channel2.basic_publish(exchange = '', routing_key = 'database', body = json.dumps(ridedetails))
    channel.close()
    channel2.close()
    return "recieved form details"

@app.route('/new_ride_matching_consumer', methods = ['POST'])
def ridematch():
    #printing for now, but should send this to rabbit ig
    consumersregistered = []
    req = request.get_json(force = True)
    consumersregistered.append(req)
    print("Consumer registered - ", req)
    return "recieved customer details"
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)