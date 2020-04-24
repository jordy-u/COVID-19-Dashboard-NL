# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:26:21 2020

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
from config_test import DB_connection_settings
import mysql.connector
from mysql.connector import errorcode
import logging
logging.basicConfig(filename='log_file.log',level=logging.DEBUG)

def plot_and_save(datafile,save_location="../images/",Save_name='Default',save_format="SVG"):
    date = datafile['Datum']
    aantal = datafile['Aantal']

    plt.plot(date,aantal)
    plt.gcf().autofmt_xdate()

    plt.savefig("{}{}.{}".format(save_location,Save_name,save_format))
    plt.suptitle("Corona gevallen voor gemeente {}".format(datafile.iloc[0][1]), fontsize=16)
    logging.info('File found')

def load_pandas(file_loc='-1'):
    if file_loc != -1:
        data = pd.read_csv("{}.csv".format(file_loc))
        return(data)
    else:
        logging.warning('File not found')
        
def url_path():
    return("https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_corona_in_nl") #url to source

def connect_to_database():
    cnx = mysql.connector.connect(user=DB_connection_settings.username(), password=DB_connection_settings.password(),
                              host=DB_connection_settings.host(),
                              database=DB_connection_settings.database())
    
    return(cnx)