# Add column indicating if data was missing
KIAH['missing'] = '0'

# Add missing dates to station sub-frame
time = pd.date_range(start = '2015-01-01', end = '2021-04-20', freq='D' )
sTime = pd.Series(index=time)
KIAH = pd.concat([KIAH, sTime[~sTime.index.isin(KIAH.index)]]).sort_index()
KIAH = KIAH.drop([0],axis=1)

# Find rows where data is missing
missingKIAH = KIAH.loc[KIAH['missing'].isna() ]
# Set values in missing subset 
# Set missing to 1
missingKIAH.loc[:,'missing'] = '1'

# Set name to station name
missingKIAH.loc[:, 'name'] = 'Houston'

# Set region to station region
missingKIAH.loc[:, 'region'] = '3'

# Set state to station state
missingKIAH.loc[:, 'state'] = 'Texas'

# Set station_code to station
missingKIAH.loc[:, 'station_code'] = 'KIAH'

# Remove empty columns of temp data
missingKIAH.drop(columns=['temp_min_c', 'temp_mean_c', 'temp_max_c', 'location_date'], inplace=True, axis=0)

#Interpolate temp_min_c within KIAH set 
KIAHinterpolMIN = KIAH['temp_min_c'].interpolate()

#Interpolate temp_max_c within KIAH set 
KIAHinterpolMAX = KIAH['temp_max_c'].interpolate()

#Interpolate temp_mean_c within KIAH set 
KIAHinterpolMEAN = KIAH['temp_mean_c'].interpolate()

# Concatenate sub-frames of interpolated temperature data into single frame
KIAHinterpol = pd.concat([KIAHinterpolMAX, KIAHinterpolMIN, KIAHinterpolMEAN], axis=1)

# Create new empty frame and integrate missing date row frames with interpolated temp frame
KIAH2 = []
KIAH2 = pd.DataFrame(s)
KIAH2 = pd.concat([KIAHinterpol, missingKIAH], axis=1)
KIAH2 = KIAH2.dropna()

# Drop all NaN rows from original station subframe and combine cleaned and interpolated subframes
KIAH = KIAH.dropna()
KIAH3 = pd.concat([KIAH, KIAH2], axis=0)
# Review complete sub-frame of KIAH 
print(KIAH3)