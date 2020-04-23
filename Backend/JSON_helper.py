# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:09:11 2020

@author: User
"""



"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: structure_for_date

Purpose: Structure an SQL data array containing a set of Gemeentecode and Aantal 
and structure it into an target array in such a way that the JSON file can be generated

Expected input: Date as Datetime.date format, Target Array as array, Source as SQL list

Expected output: target array as array

Dependancies: none

"""

def structure_for_date(Date, Target, Source):
    temp_data_set ={}
    for Gemeentecode, Aantal in Source:
        temp_data_set[str(Gemeentecode)] = Aantal
    Target[str(Date)] = temp_data_set
    return(Target)
"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: save_JSON

Purpose: save a given structured array as JSON file to the drive

Expected input: Target Array as array, file name as string, possible alternative location as string

Expected output: File saved file in /outputs/[filename].json
    
Dependancies: json library
"""
import json
def save_JSON(target, filename="output", location = "../outputs/"):
    with open('{}{}.json'.format(location,filename), 'w') as outfile:
            json.dump(target, outfile)
"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: structure_array

Purpose: get an array of dates and get the corrosponding data from the database, 
Structure this data into an array for the json export

Expected input: table name as string, SQL query result as array, object for mysql helper to initialize the cursor

Expected output: structured array for JSON save.
    
Dependancies: mysql connect
"""
import mysql.connector

def structure_array(table_name, source, cnx):
    json_output_data = {}
    sellect_all_gemeentes_per_date = ("SELECT Gemeentecode, Aantal FROM `{}` WHERE Datum ='{}'")
    search_for_datum_cursor = cnx.cursor()
    for Datum in source:
        search_for_datum_cursor.execute(sellect_all_gemeentes_per_date.format(table_name,Datum[0]))
        json_output_data=structure_for_date(Datum[0],json_output_data,search_for_datum_cursor)
    return json_output_data
"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: get_date

Purpose: to get all unique dates from a database

Expected input: table name as string , object for mysql helper to initialize the cursor

Expected output: sql array
    
Dependancies: mysql connect
"""
def get_date(table_name, cnx):
    select_all_datums_in_database = ("SELECT DISTINCT Datum FROM {} ORDER BY Datum ASC")
    check_datum_cursor = cnx.cursor()
    check_datum_cursor.execute(select_all_datums_in_database.format(table_name)) #select all Unique datums from the database
    return check_datum_cursor.fetchall()
"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: create_json

Purpose: phrase an JSON file from a table name

Expected input: table name as string, json storagename as string , object for mysql helper to initialize the cursor

Expected output: sql array
    
Dependancies: mysql connect and json
"""
def create_json(table_name,filename ,cnx):
    result = get_date(table_name, cnx)
    json_output_data = structure_array(table_name,result, cnx)
    save_JSON(json_output_data,filename)
