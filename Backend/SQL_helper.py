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
from log_lib import event
def insert_new_entry(table_name, datum, gemeentecode, aantal, cnx):
    insert_new_data_query = ("INSERT INTO `%s` (`Datum`, `Gemeentecode`, `Aantal`) VALUES (%s, %s, %s)")
    inser_cursor = cnx.cursor()
    inser_cursor.execute(insert_new_data_query,(table_name, datum, gemeentecode,aantal))
    event.new_entry(datum,gemeentecode)
    
"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: does_table_exist

Purpose: to check if the given table exists

Expected input: table name as string, mysql object for cursor

Expected output: boolean ouput if the table exists

Dependancies: mysql connect

"""
def does_table_exist(table_name, cnx):
    search_query = ("SHOW TABLES LIKE '{}'")
    search_cursor = cnx.cursor()
    search_cursor.execute(search_query.format(table_name))
    return search_cursor.fetchone() != None
    