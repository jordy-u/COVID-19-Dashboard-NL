# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:08:21 2020

@author: Laurens Roos
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
from JSON_helper import *

logging.basicConfig(filename='log_file.log',level=logging.DEBUG)
logging.info('Start program')

table_list = [   
    ['Corona_per_gemeente','covid19_reports_every_day','https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_corona_in_nl'],
    ['ziekenhuis_opname_per_gemeente','covid19_hospitalizations','']
             ]

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
    #all cursors are loaded
    
    create_json(table_list[0][0],table_list[0][1],cnx)
    
    cnx.commit()
    cnx.close()
    