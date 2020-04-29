# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:08:21 2020

@author: Laurens Roos
"""


import pandas as pd
from setup import *
from config import *
import mysql.connector
from mysql.connector import errorcode
import logging
import json
from JSON_helper import *
from SQL_helper import *
from CSV_helper import *

logging.basicConfig(filename='log_file.log',level=logging.DEBUG)
logging.info('Start program')

# list with tabels as source. following the syntax: Table name, JSON name, SOURCE CSV
table_list = [   
    ['corona_per_gemeente_totaal','covid19_reports_every_day','https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_NL_covid19_total_municipality'],
    ['ziekenhuis_opname_per_gemeente_totaal','covid19_hospitalizations','https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_NL_covid19_hosp_municipality']
             ]



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
    #start_time = time.time()
    for packet in table_list:

        if does_table_exist(packet[0], cnx) != True: #making sure that the table already exists
            create_new_table_for_gemeente(packet[0], cnx)
            logging.info("No table found with entry for {}. Table is generated".format(packet[0]))
        for index, row in get_CSV_data(packet[2]).iterrows(): #from the CSV source, get all the info and split them into rows.
             data_compaired+=1
             if does_entry_exist(packet[0],row['Datum'],row['Gemeentecode'],cnx) != True: #check if the entry already exists or not
                 insert_new_entry(packet[0],row['Datum'], row['Gemeentecode'], row['Aantal'], cnx)
                 new_entries+=1
        
        if new_entries != 0: #only if new entries have been added, generate a new JSON
            logging.info("{} Entries found, updating JSON".format(new_entries))
            create_json(packet[0],packet[1],cnx, '../public/assets/NL_kaart/')
        else :
            logging.info("no new entries found, Exit program without JSON updates.")
    cnx.commit()
    cnx.close()
    