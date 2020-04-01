# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:37 2020

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
from setup import *
from log_lib import *
from config_test import *
import time
import mysql.connector
from mysql.connector import errorcode

data = load_pandas(url_path())
query = ("SELECT Datum, Gemeentecode, Aantal FROM corona_in_nl WHERE Datum =%s AND Gemeentecode =%s")

try:
    cnx=connect_to_database()
    
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    event.invalid_login()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    event.invalid_database()
  else:
    print(err)
else:
    cursor = cnx.cursor()
    start_time = time.time()
    
    for index, row in data.iterrows():
        cursor.execute(query, (row['Datum'],row['Gemeentecode']))
        for (Datum, Gemeentecode, Aantal) in cursor:
           print("bla")
    print('operation took {} seconds to complete'.format(time.time()-start_time))