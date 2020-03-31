# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:02:06 2020

@author: User
"""


from config import DB_connection_settings

import mysql.connector
import mysql.connector



cnx = mysql.connector.connect(user=DB_connection_settings.username(), password=DB_connection_settings.password(),
                              host=DB_connection_settings.host(),
                              database='test')
cursor = cnx.cursor()

query = ("SELECT * FROM test")

cursor.execute(query)

for (ID,text) in cursor:
    print(ID, "   " ,text)

cnx.close()