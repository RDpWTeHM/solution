#!/usr/bin/env python3
import pika


HOST_ADDR = 'localhost'
QUEUE = 'hello'
TAG = 'hello'

def setup():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST_ADDR))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE)

    return connection, channel


def callback(ch, method, properties, body):
    body = body.decode()
    if body == "quit":
        ch.basic_cancel(consumer_tag=TAG)
        ch.stop_consuming()
    else:
        print(" [x] Received %r" % body)


def main():
    connection, channel = setup()

    channel.basic_consume(
        queue=QUEUE, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages......')
    print('\tTo exit press CTRL+C, or send "quit" message')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.basic_cancel(consumer_tag=TAG)
        channel.stop_consuming()

if __name__ == "__main__":
    main()

