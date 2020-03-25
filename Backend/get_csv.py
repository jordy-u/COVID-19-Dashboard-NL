# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:24:33 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdatas
print("reading file")
path_to_file="../data/rivm_corona_in_nl_daily.csv"
save_location="../images/daily_corona_cases"
try:
    data = pd.read_csv(path_to_file)
except pd.errors.FileNotFoundError:
        print("file read error")
        pass
else:
    print("file found")

print(data.head())
date = data['Datum']
aantal = data['Aantal']

plt.plot(date,aantal)
plt.gcf().autofmt_xdate()

plt.savefig("{}.SVG".format(save_location))

