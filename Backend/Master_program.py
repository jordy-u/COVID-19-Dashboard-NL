# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:08:21 2020

@author: User
"""


import pandas as pd
#import matplotlib.pyplot as plt
from setup import *
#from log_lib import *
from config_test import *
#import time
import mysql.connector
from mysql.connector import errorcode
import logging
from datetime import datetime
import json

logging.basicConfig(filename='log_file.log',level=logging.DEBUG)
logging.info('Start program')

query = ("SELECT Datum, Gemeentecode, Aantal FROM Corona_per_gemeente WHERE Datum =%s AND Gemeentecode =%s")
insert_new_data_query = ("INSERT INTO `Corona_per_gemeente` (`Datum`, `Gemeentenaam`, `Gemeentecode`, `Provincienaam`, `Aantal`) VALUES (%s, %s, %s, %s, %s)")
select_all_datums_in_database = ("SELECT DISTINCT Datum FROM {} ORDER BY Datum ASC")
sellect_all_gemeentes_per_date = ("SELECT Gemeentecode, Aantal FROM `Corona_per_gemeente` WHERE Datum ='{}'")

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
    """
    Loading all cusors for the database connection. Since the cursor holds all the data requested from the database.
    It is ideal to have a cursor per type of operation
    """
    cursor = cnx.cursor()
    inser_cursor = cnx.cursor()
    check_datum_cursor = cnx.cursor()
    search_for_datum_cursor = cnx.cursor()
    
    #all cursors are loaded
    
    
    check_datum_cursor.execute(select_all_datums_in_database.format('Corona_per_gemeente')) #select all Unique datums from the database
    result = check_datum_cursor.fetchall()
    json_output_data = {}
    for Datum in result:
        print(Datum[0])
        search_for_datum_cursor.execute(sellect_all_gemeentes_per_date.format(Datum[0]))
        temp_data_set ={}
        for Gemeentecode, Aantal in search_for_datum_cursor:
            temp_data_set['{}'.format(Gemeentecode)] = Aantal
        json_output_data['{}'.format(Datum[0])] = temp_data_set
        print(json.dumps(json_output_data))
        with open('output.json', 'w') as outfile:
            json.dump(json_output_data, outfile)
    cnx.commit()
    cnx.close()
    