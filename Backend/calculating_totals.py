# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:43:08 2020

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
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.info('Start program')


query = ("SELECT Datum, Gemeentecode, Aantal FROM Corona_per_gemeente ORDER BY Gemeentecode")
query_2 = ("SELECT Gemeentecode,Totaal FROM corona_totaal_per_gemeente WHERE Gemeentecode ={}")

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
    second_sellect = cnx.cursor()
    start_time = time.time()
    cursor.execute(query)
    bla = cursor.fetchall()
    print(bla)
    for (Datum, Gemeentecode, Aantal) in bla:
        second_sellect.execute(query_2.format(Gemeentecode))
        if second_sellect.fetchone() == None:
            print("Gemeente {} niet in de database gevonden".format(Gemeentecode))
   
    cnx.close()