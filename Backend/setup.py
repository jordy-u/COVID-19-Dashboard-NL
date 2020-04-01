# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:55 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
from log_lib import *


def plot_and_save(datafile,save_location="../images/",Save_name='Default',save_format="SVG"):
    date = datafile['Datum']
    aantal = datafile['Aantal']

    plt.plot(date,aantal)
    plt.gcf().autofmt_xdate()

    plt.savefig("{}{}.{}".format(save_location,Save_name,save_format))
    plt.suptitle("Corona gevallen voor gemeente {}".format(datafile.iloc[0][1]), fontsize=16)
    even.file_found()

def load_pandas(file_loc='-1'):
    if file_loc != -1:
        data = pd.read_csv("{}.csv".format(file_loc))
        return(data)
    else:
        event.file_not_found()
        
def url_path():
    return("https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_corona_in_nl") #url to source