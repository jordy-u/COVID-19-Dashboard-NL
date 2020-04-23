# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:21:30 2020

@author: laurens Roos
"""

"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: insert_new_entry

Purpose: to insert new entries into a given table

Expected input: table name as string, Datum as datetime.date, gemeentecode as string, aantal as int, mysql object for cursor

Expected output: sql querries to insert into a database

Dependancies: mysql connect, log_lib

"""
from log_lib import new_entry
def insert_new_entry(table_name, datum, gemeentecode, aantal, cnx):
    insert_new_data_query = ("INSERT INTO `%s` (`Datum`, `Gemeentecode`, `Aantal`) VALUES (%s, %s, %s)")
    inser_cursor = cnx.cursor()
    inser_cursor.execute(insert_new_data_query,(table_name, datum, gemeentecode,aantal))
    event.new_entry(datum,gemeentecode)
    