from typing import Any, Dict, List

import pandas as pd
import csv
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.task_group import TaskGroup
from sqlalchemy import create_engine

from time import sleep
import hashlib
import requests
import json
import os

priv_key = '7f5c22629bc15ebeb50123a7dfe5425dba43984f'
pub_key = '13661f5daa8d05f9abe2a42a67cd27b5'
timestamp = '10'

combined_keys = timestamp + priv_key + pub_key
md5hash = hashlib.md5(combined_keys.encode()).hexdigest()

# Get function to retrive data
def get_api_marvel(endpoint):
    #sleep(2)
    url = f'https://gateway.marvel.com:443/v1/public/{endpoint}?ts={timestamp}&apikey={pub_key}&hash={md5hash}'
    try:
        r = requests.get(url)
        out_json = r.json()
        error = False
    except ConnectionError as e:
        print("CONNECTION ERROR: ")
        print(e)
        out_json = ''
        error = True
    write_json(endpoint, out_json)
    #return out_json, error

    
#Save file in airflow docker
def write_json(endpoint,out_json):
      with open(
        os.path.join('/opt/airflow/dags/files', f'{endpoint}_data.json'), 'w'
    ) as outfile:
        outfile.write(((json.dumps(out_json['data']['results']))) + '\n')

#Read file
def read_json_characters():
    with open('/opt/airflow/dags/files/characters_data.json') as json_file:
        jsondata = json.load(json_file)
    
    data_file = open('/opt/airflow/dags/files/characters_data.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
 
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
 
    data_file.close()

#Read file
def read_json_comics():
    with open('/opt/airflow/dags/files/comics_data.json') as json_file:
        jsondata = json.load(json_file)
    
    data_file = open('/opt/airflow/dags/files/comics_data.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
 
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
 
    data_file.close()

