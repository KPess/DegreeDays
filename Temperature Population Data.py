import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

filename = 'Temp Data.csv'
df_temp = pd.read_csv('../SynMax/Temp Data.csv')
df_temp = df_temp.set_index('datetime')
ts_tempMin = df_temp['temp_min_c']
ts_tempMax = df_temp['temp_max_c']
ts_tempMean = df_temp['temp_mean_c']

print(ts_tempMax)