from fastapi import (
    APIRouter
)
from json import dumps
from faker import Faker
import collections
import json

router = APIRouter(

)
@router.get('/data/generate/{size}')
def get_data(size:int):
    def fake_person_generator(length, fake):
        for x in range(length):  # xrange in Python 2.7
            yield {'last_name': fake.last_name(),
                'first_name': fake.first_name(),
                'street_address': fake.street_address(),
                'email': fake.email(),
                'index': x}

    filename = f'{size}_persons'

    fake     = Faker() # 
    fpg = fake_person_generator(size, fake)
    with open('%s.json' % filename, 'w') as output:
        output.write('[')  # to made json file valid according to JSON format
        for i,person in enumerate(fpg):
            json.dump(person, output)
            if i!=size-1:
                 output.write(',')
        output.write(']')  # to made json file valid according to JSON format
    return ""

@router.get('/data/get/{size}/{page}')
def get_data(size:int,
             page:int):
    with open('1M.json') as f:
       data=json.load(f)
    return data[(page-1)*size:page*size]