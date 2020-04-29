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
    insert_new_data_query = ("INSERT INTO {} (`Datum`, `Gemeentecode`, `Aantal`) VALUES ('{}', '{}', '{}')")
    inser_cursor = cnx.cursor()
    inser_cursor.execute(insert_new_data_query.format(table_name, datum, gemeentecode,aantal))
    cnx.commit()
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

"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: create_new_table_for_gemeente

Purpose: create a new table for the aantalen per gemeente with the correct structure

Expected input: table name as string, mysql object for cursor

Expected output: mysql generated table in the database

Dependancies: mysql connect

"""
def create_new_table_for_gemeente(table_name, cnx):
    creation_query = ("CREATE TABLE {} ( `ID` INT NOT NULL AUTO_INCREMENT , `Datum` DATE NOT NULL , `Gemeentecode` INT NOT NULL , `Aantal` INT NOT NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB")
    creation_cursor = cnx.cursor()
    creation_cursor.execute(creation_query.format(table_name))
    
"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: does_entry_exist

Purpose: check if the entry already exists

Expected input: table name as string, datum as datetime.date, gemeentecode as string, mysql object for cursor

Expected output: boolean if the entry exists

Dependancies: mysql connect

"""
def does_entry_exist(table_name,date,gemeentecode,cnx):
    search_query = ("SELECT Datum, Gemeentecode, Aantal FROM {} WHERE Datum ='{}' AND Gemeentecode ='{}'")
    search_cursor = cnx.cursor()
    search_cursor.execute(search_query.format(table_name, date, gemeentecode))
    return search_cursor.fetchone() != None
    
  