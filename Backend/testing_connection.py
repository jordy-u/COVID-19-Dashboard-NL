# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:02:06 2020

@author: User
"""


from config import DB_connection_settings

import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user=DB_connection_settings.username(), password=DB_connection_settings.password(),
                              host=DB_connection_settings.host(),
                              database='test')
    
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM test")
    query2 = ("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema='[database]' AND table_name='[table_name]'")
    cursor.execute(query)
    
    for (ID,time,text) in cursor:
        print("Data gevonden, tegevoegt op {}, met ID {}, Data is alsvolgt {}".format(time,ID,text))
    
    cnx.close()