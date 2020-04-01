# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:24:33 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_and_save(datafile,save_location="../images/",Save_name='Default',save_format="SVG"):
    date = datafile['Datum']
    aantal = datafile['Aantal']

    plt.plot(date,aantal)
    plt.gcf().autofmt_xdate()

    plt.savefig("{}{}.{}".format(save_location,Save_name,save_format))
    plt.suptitle("Corona gevallen voor gemeente {}".format(datafile.iloc[0][1]), fontsize=16)
    print("file created")

def load_pandas(file_loc='-1'):
    if file_loc != -1:
        data = pd.read_csv("{}.csv".format(path_to_file))
        return(data)
    else:
        print("no file path fiven")

print("reading file")
path_to_file="https://raw.githubusercontent.com/J535D165/CoronaWatchNL/master/data/rivm_corona_in_nl"
path_to_save="../images/daily_corona_cases"

data = load_pandas(path_to_file)

g_code = int(input("Voer gemeentecode in : "))

gemeente_geselecteerde_data = data.loc[data['Gemeentecode'] == g_code]

if gemeente_geselecteerde_data.empty != True:
    print("Uw gemeentecode is {} , De geselecteerde gemeente is {} Wij halen nu de data op".format(g_code, gemeente_geselecteerde_data.iloc[0][1]))
    print(gemeente_geselecteerde_data.head())
    plot_and_save(gemeente_geselecteerde_data,Save_name=g_code)
else:
    print("Geen corona in gemeente met code {} gevonden".format(g_code))

