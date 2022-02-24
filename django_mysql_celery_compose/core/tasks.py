from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(15)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def say_hello():
    print('Hello Docker Compose')
