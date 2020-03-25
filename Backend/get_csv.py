# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:24:33 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdatas

def plot_and_safe(datafile,save_location="../images/daily_corona_cases",save_format=".SVG"):
    date = datafile['Datum']
    aantal = datafile['Aantal']

    plt.plot(date,aantal)
    plt.gcf().autofmt_xdate()

    plt.savefig("{}.{}".format(save_location,save_format))
    print("file created")


print("reading file")
path_to_file="../data/rivm_corona_in_nl_daily"
path_to_save="../images/daily_corona_cases"

try:
    data = pd.read_csv("{}.csv".format(path_to_file))
except pd.errors.FileNotFoundError:
        print("file read error")
        pass
else:
    print("file found")

print(data.head())


plot_and_safe(data)