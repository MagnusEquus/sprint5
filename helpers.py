import random


def generate_email():
    number = random.randint(100,99999)
    email = f'123+{number}@yandex.ru'
    return email


def generate_pass():
    password = random.randint(100000, 999999999)
    return password