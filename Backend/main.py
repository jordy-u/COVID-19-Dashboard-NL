# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:37 2020

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
from setup import *
from log_lib import *
from config import *
import time
import mysql.connector
from mysql.connector import errorcode
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.info('Start program')

data = load_pandas(url_path())
query = ("SELECT Datum, Gemeentecode, Aantal FROM Corona_per_gemeente WHERE Datum =%s AND Gemeentecode =%s")
insert_new_data_query = ("INSERT INTO `Corona_per_gemeente` (`Datum`, `Gemeentenaam`, `Gemeentecode`, `Provincienaam`, `Aantal`) VALUES (%s, %s, %s, %s, %s)")

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
    inser_cursor = cnx.cursor()
    start_time = time.time()
    
    for index, row in data.iterrows():
        data_compaired+=1
        cursor.execute(query, (row['Datum'],row['Gemeentecode']))
        if cursor.fetchone() != None:
           existing_entries+=1
        else:
            new_entries+=1
            logging.info('New entry found on timestamp {}'.format(time.time()))
            if row['Gemeentecode'] != -1:
                inser_cursor.execute(insert_new_data_query,(row['Datum'],row['Gemeentenaam'],row['Gemeentecode'],row['Provincienaam'],row['Aantal']))
            else:
                inser_cursor.execute(insert_new_data_query,(row['Datum'],'NULL',row['Gemeentecode'],'NULL',row['Aantal']))
            event.new_entry(row['Datum'],row['Gemeentecode'])
    cnx.commit()
    logging.info('operation took {} seconds to complete. Searched trough {} entries, Found {} matching entries and created {} new entries'.format(time.time()-start_time,data_compaired,existing_entries,new_entries))
    cnx.close()