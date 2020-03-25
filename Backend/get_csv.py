# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:24:33 2020

@author: User
"""

import pandas as pd

print("reading file")
path_to_file="../data/rivm_corona_in_nl.csv"

try:
    data = pd.read_csv(path_to_file)
except pd.errors.FileNotFoundError:
        print("file read error")
        pass
else:
    print("file found")
    

print(data.head())



