#!/usr/bin/env python3
import sys
import pika


HOST_ADDR = 'localhost'
QUEUE = 'hello'
KEY = 'hello'


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST_ADDR))
channel = connection.channel()

channel.queue_declare(queue=QUEUE)

try:
    msg = sys.argv[1]
except:
    msg = "Hello World!"

channel.basic_publish(
    exchange='',
    routing_key=KEY,
    body=msg)

print(" [x] Sent '{}'".format(msg))
connection.close()

