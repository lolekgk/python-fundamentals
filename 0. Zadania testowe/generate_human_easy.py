import random
import string
from uuid import uuid4
from pprint import pprint

from names import get_first_name, get_last_name


def generate_country():
    with open('countries.txt', 'r') as f:
        countries = f.read().splitlines()

    return random.choice(countries).title()


def generate_phone_number():
    random_digits = random.choices(string.digits, k=9)
    return int(''.join(random_digits))


def generate_human():
    keys = ['name', 'surname', 'email', 'age', 'phone_number', 'country', 'id']
    name, surname = get_first_name(), get_last_name()
    values = [
        name,
        surname,
        f'{name}{surname}@gmail.com'.lower(),
        random.randint(18, 85),
        generate_phone_number(),
        generate_country(),
        str(uuid4()),
    ]

    return {k: v for k, v in zip(keys, values)}


pprint(generate_human())
