import pandas as pd
import numpy as np

time_classes = {
    'Early Morning': (0, 6),
    'Morning': (6, 9),
    'Late Morning': (9, 12),
    'Afternoon': (12, 15),
    'Evening': (15, 18),
    'Night': (18, 21),
    'Late Night': (21, 24)
}

def classify_hour(hour):
    for class_name, (start, end) in time_classes.items():
        if start <= hour < end:
            return class_name
    return None

initial_df = pd.read_csv('./data/incident-response.csv')

processed_df = initial_df.copy()

processed_df['CITY'] = processed_df['INCIDENT_LOCATION'].str.split(',').str[1].str.strip()

processed_df['DATE'] = processed_df['INCIDENT_DATETIME'].str.split(' ').str[0]
processed_df['TIME'] = processed_df['INCIDENT_DATETIME'].str.split(' ').str[1] + " " + processed_df['INCIDENT_DATETIME'].str.split(' ').str[2]

processed_df['HOUR'] = pd.to_datetime(processed_df['TIME'], format='%I:%M:%S %p').dt.hour

processed_df['TIME_OF_DAY'] = processed_df['HOUR'].apply(classify_hour)

processed_df['IS_FALSE_ALARM'] = (processed_df['INITIAL_INCIDENT_TYPE'] == 'ALARMS') & (processed_df['INITIAL_INCIDENT_TYPE'] != processed_df['FINAL_INCIDENT_TYPE'])
processed_df['IS_FALSE_ALARM'] = np.where(processed_df['INITIAL_INCIDENT_TYPE'] == 'ALARMS', processed_df['IS_FALSE_ALARM'], 'NA')

processed_df = processed_df[['INCIDENT_NUMBER', 'INCIDENT_DATETIME',
       'INCIDENT_LOCATION', 'INITIAL_INCIDENT_TYPE', 'FINAL_INCIDENT_TYPE',
       'INITIAL_RESPONSE', 'CITY', 'DATE', 'TIME', 'HOUR',
       'TIME_OF_DAY', 'IS_FALSE_ALARM']]

processed_df.to_csv('./data/processed_incident.csv')