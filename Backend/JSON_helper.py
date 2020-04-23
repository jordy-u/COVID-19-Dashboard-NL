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

Name: 

Purpose: 

Expected input: 

Expected output: 
    
Dependancies:
"""

