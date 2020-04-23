# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:08:21 2020

@author: Laurens Roos
"""


import pandas as pd
from setup import *
from config_test import *
import mysql.connector
from mysql.connector import errorcode
import logging
import json
from JSON_helper import *
from SQL_helper import *

logging.basicConfig(filename='log_file.log',level=logging.DEBUG)
logging.info('Start program')

table_list = [   
    ['Corona_per_gemeente','covid19_reports_every_day','https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_corona_in_nl'],
    ['ziekenhuis_opname_per_gemeente','covid19_hospitalizations','']
             ]

query = ("SELECT Datum, Gemeentecode, Aantal FROM Corona_per_gemeente WHERE Datum =%s AND Gemeentecode =%s")



existing_entries = 0
new_entries = 0
data_compaired = 0

try:
    cnx=connect_to_database()
    
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    logging.warning("invalid_login")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    logging.warning("invalid database")
  else:
    logging.warning(err)
else:
    cursor = cnx.cursor()
    #all cursors are loaded
    inser_cursor = cnx.cursor()
    start_time = time.time()
    
    for index, row in data.iterrows():
        data_compaired+=1
        cursor.execute(query, (row['Datum'],row['Gemeentecode']))
        if cursor.fetchone() != None:
           existing_entries+=1
        else:
            insert_new_entry()
            new_entries+=1
            logging.info('New entry found on timestamp {}'.format(time.time()))
            
    if new_entries != 0:
        create_json(table_list[0][0],table_list[0][1],cnx)
    
    cnx.commit()
    cnx.close()
    