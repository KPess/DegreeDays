# Add column indicating if data was missing
KATL['missing'] = '0'

# Add missing dates to station sub-frame
time = pd.date_range(start = '2015-01-01', end = '2021-04-20', freq='D' )
sTime = pd.Series(index=time)
KATL = pd.concat([KATL, sTime[~sTime.index.isin(KATL.index)]]).sort_index()
KATL = KATL.drop([0],axis=1)

# Find rows where data is missing
missingKATL = KATL.loc[KATL['missing'].isna() ]
# Set values in missing subset 
# Set missing to 1
missingKATL.loc[:,'missing'] = '1'

# Set name to station name
missingKATL.loc[:, 'name'] = 'Atlanta'

# Set region to station region
missingKATL.loc[:, 'region'] = '6'

# Set state to station state
missingKATL.loc[:, 'state'] = 'Georgia'

# Set station_code to station
missingKATL.loc[:, 'station_code'] = 'KATL'

# Remove empty columns of temp data
missingKATL.drop(columns=['temp_min_c', 'temp_mean_c', 'temp_max_c', 'location_date'], inplace=True, axis=0)

#Interpolate temp_min_c within KATL set 
KATLinterpolMIN = KATL['temp_min_c'].interpolate()

#Interpolate temp_max_c within KATL set 
KATLinterpolMAX = KATL['temp_max_c'].interpolate()

#Interpolate temp_mean_c within KATL set 
KATLinterpolMEAN = KATL['temp_mean_c'].interpolate()

# Concatenate sub-frames of interpolated temperature data into single frame
KATLinterpol = pd.concat([KATLinterpolMAX, KATLinterpolMIN, KATLinterpolMEAN], axis=1)

# Create new empty frame and integrate missing date row frames with interpolated temp frame
KATL2 = []
KATL2 = pd.DataFrame(s)
KATL2 = pd.concat([KATLinterpol, missingKATL], axis=1)
KATL2 = KATL2.dropna()

# Drop all NaN rows from original station subframe and combine cleaned and interpolated subframes
KATL = KATL.dropna()
KATL3 = pd.concat([KATL, KATL2], axis=0)
# Review complete sub-frame of KATL 
print(KATL3)