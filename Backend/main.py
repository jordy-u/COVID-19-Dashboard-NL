# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:37 2020

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
from setup import *
from log_lib import *
from config_test import *
import time

data = load_pandas(url_path())

start_time = time.time()
for index, row in data.iterrows():
    print("Nieuw corona geval op {} geconstateerd in gemeente {}. Aantral gevallen = {}".format(row['Datum'], row['Gemeentenaam'], row['Aantal']))
print('operation took {} seconds to complete'.format(time.time()-start_time))