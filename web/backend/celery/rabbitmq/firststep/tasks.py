# tasks.py

from celery import Celery

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
app = Celery('tasks', broker=BROKER_URL)


@app.task
def add(x, y):
    return x + y
