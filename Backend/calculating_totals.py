# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:43:08 2020

@author: User
"""
from setup import connect_to_database
from config_test import *
import time
import mysql.connector
from mysql.connector import errorcode
import logging
logging.basicConfig(filename='calculation_log.log',level=logging.DEBUG)
logging.info('Start program')

Compaired = 0
Updated = 0
New_entries = 0

query = ("SELECT Datum,Gemeentenaam, Gemeentecode, Aantal FROM Corona_per_gemeente ORDER BY Gemeentecode ASC, Datum ASC")
query_2 = ("SELECT Gemeentecode, Update_date,Totaal FROM corona_totaal_per_gemeente WHERE Gemeentecode ={}")
insert_new_table = ("INSERT INTO `corona_totaal_per_gemeente` (`Gemeentecode`, `Gemeentenaam`, `Update_date`, `Totaal`) VALUES (%s, %s, %s, %s)")
update_table = ("UPDATE `corona_totaal_per_gemeente` SET Update_date = %s, Totaal = %s WHERE Gemeentecode = %s")

info_string=("Operation complete! Operation took: {} Seconds, Compaired {} Items, Added {} New items and Updated {} Items")

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
    start_time = time.time()
    cursor = cnx.cursor()
    second_sellect = cnx.cursor()
    insert_cursor = cnx.cursor()
    start_time = time.time()
    cursor.execute(query)
    bla = cursor.fetchall()
    for (Datum, Gemeentenaam ,Gemeentecode, Aantal) in bla:
        print(Gemeentecode, Datum)
        second_sellect.execute(query_2.format(Gemeentecode))
        data = second_sellect.fetchone()
        Compaired +=1
        if data == None:
            logging.info("Gemeente {} niet in de database gevonden Update datum = {}".format(Gemeentecode, Datum))
            insert_cursor.execute(insert_new_table,(Gemeentecode,Gemeentenaam,Datum,Aantal))
            New_entries+=1
        
        elif data[1] < Datum :
            logging.info("{} < {} Datum is outdated".format(data[1],Datum))
            insert_cursor.execute(update_table,(Datum, data[2]+Aantal, Gemeentecode))
            Updated+=1
        else:
            logging.info("Compaired and up to date")
    cnx.commit()
    end_time = time.time()-start_time
    logging.info(info_string.format(end_time,Compaired,New_entries,Updated))
    print(info_string.format(end_time,Compaired,New_entries,Updated))
    cnx.close()