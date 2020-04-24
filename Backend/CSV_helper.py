# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:31:38 2020

@author: Laurens Roos
"""


"""
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

Name: get_CSV_data

Purpose: getting and returning the data from the file path 

Expected input: file path as string 

Expected output: CSV data as pandas array

Dependancies: Pandas logging

"""
import pandas as pd
import logging

def get_CSV_data(file_loc = '-1'):
    if file_loc != -1:
        data = pd.read_csv("{}.csv".format(file_loc))
        logging.info("CSV loaded")
        return(data)
    else:
        logging.info("no file path fiven")
