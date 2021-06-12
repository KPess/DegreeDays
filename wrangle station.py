# Add column indicating if data was missing
KSTL['missing'] = '0'

# Add missing dates to station sub-frame
time = pd.date_range(start = '2015-01-01', end = '2021-04-20', freq='D' )
sTime = pd.Series(index=time)
KSTL = pd.concat([KSTL, sTime[~sTime.index.isin(KSTL.index)]]).sort_index()
KSTL = KSTL.drop([0],axis=1)

# Find rows where data is missing
missingKSTL = KSTL.loc[KSTL['missing'].isna() ]
# Set values in missing subset 
# Set missing to 1
missingKSTL.loc[:,'missing'] = '1'

# Set name to station name
missingKSTL.loc[:, 'name'] = 'St Louis/Lambert'

# Set region to station region
missingKSTL.loc[:, 'region'] = '2'

# Set state to station state
missingKSTL.loc[:, 'state'] = 'Missouri'

# Set station_code to station
missingKSTL.loc[:, 'station_code'] = 'KSTL'

# Remove empty columns of temp data
missingKSTL.drop(columns=['temp_min_c', 'temp_mean_c', 'temp_max_c', 'location_date'], inplace=True, axis=0)

#Interpolate temp_min_c within KSTL set 
KSTLinterpolMIN = KSTL['temp_min_c'].interpolate()

#Interpolate temp_max_c within KSTL set 
KSTLinterpolMAX = KSTL['temp_max_c'].interpolate()

#Interpolate temp_mean_c within KSTL set 
KSTLinterpolMEAN = KSTL['temp_mean_c'].interpolate()

# Concatenate sub-frames of interpolated temperature data into single frame
KSTLinterpol = pd.concat([KSTLinterpolMAX, KSTLinterpolMIN, KSTLinterpolMEAN], axis=1)

# Create new empty frame and integrate missing date row frames with interpolated temp frame
KSTL2 = []
KSTL2 = pd.DataFrame(s)
KSTL2 = pd.concat([KSTLinterpol, missingKSTL], axis=1)
KSTL2 = KSTL2.dropna()

# Drop all NaN rows from original station subframe and combine cleaned and interpolated subframes
KSTL = KSTL.dropna()
KSTL3 = pd.concat([KSTL, KSTL2], axis=0)
# Review complete sub-frame of KSTL 
print(KSTL3)