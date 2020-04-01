# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:38:40 2020

@author: User
"""


class event:
    
    def file_not_found():
        print("file read error")
    
    def file_found():
        print("file found")
    def invalid_login():
        print("Something is wrong with your user name or password")
    def invalid_database():
        print("Database does not exist")
    def new_entry(Datum,Gemeentecode):
        print("Creating new entry on date {}, with code {}".format(Datum, Gemeentecode))