# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## LIBRARIES

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

## IMPORT

birds = pd.read_csv("Countdata.csv")
codes = pd.read_csv("SpeciesCodes.csv")

## FUNCTIONS

def valueCount(column):
    x = column.value_counts()
    return x

def fillDown(data, column, row):
    if pd.isna(data[column][row]) and data['Point'][row] != '88':
        data.at[row, column]=data.at[row-1, column]
    else:
        pass

## VIEW

birds.columns
# 'ObserverID', 'Year', 'Month', 'Day', 'SurveyID', 'StartTime', 
# 'Point', 'Minute', 'SpeciesCode', 'Distance', 'How', 'Visual', 
# 'Sex', 'Migrating', 'ClusterSize', 'ClusterCode', 'Notes'
# make 'Start Time' 'StartTime'

for header in list(birds.columns):
    print(valueCount(birds[header]))
# Exceptions Handled 6/21/2020:
# change 'D & Q' to 'DQ' (SurveyID)
# fix '0:00' and '5^' (Point)
# fix '88.0' (Minute)
# fix 'C ' (Distance)
# fix 'C' (How)
# fix 'M', 'F', and 'J' (Visual)
# investigate inputs (Migrating)
# investigate inputs (ClusterSize)
# change dtype (ClusterSize)

birds.isna().sum().sort_values(ascending=False)
# NA's Handled 6/21/2020:
# make Y/N (Migrating, Visual)
# delete empty lines
# fill in known nans ()

## CLEAN

# make 'Start Time' 'StartTime'
birds.rename(columns={'Start Time':'StartTime'}, inplace=True)

# change 'D & Q' to 'DQ' (SurveyID)
birds['SurveyID'].replace('D & Q', 'DQ', inplace=True)

# fix '0:00' and '5^' (Point)
birds.loc[birds['Point']=='0:00'] # 743
birds.at[743, 'Point']='5'
birds.loc[birds['Point']=='5^'] # 744
birds.at[744, 'Point']='5'

# fix '88.0' (Minute)
birds.loc[birds['Minute']==88] # 271
birds.at[271, 'Minute']=float('NaN')
birds.at[271, 'Point']="88"

# fix 'C ' (Distance)
birds.loc[birds['Distance']=='C '] # 522
birds.at[522, 'Distance']=float('NaN')
birds.at[522, 'How']='C'

# fix 'C' (How)
birds.loc[birds['How']=='C '] # 812
birds.at[812, 'How']='C'

# fix 'M', 'F', and 'J' (Visual)
birds.loc[birds['Visual']=='M'] # multiple
birds.loc[birds['Visual']=='F'] # multiple
birds.loc[birds['Visual']=='J'] # 768
for letter in ['M', 'F', 'J']:
    rows = birds.loc[birds['Visual']==letter].index.to_numpy()
    for index in rows:
        birds.at[index, 'Visual']=1
        birds.at[index, 'Sex']=letter

# investigate inputs (Migrating)
for number in ['2', '4', '3', '5', '20', '40', '1', '6']:
    rows = birds.loc[birds['Migrating']==number].index.to_numpy()
    for index in rows:
        birds.at[index, 'Migrating']=0
        birds.at[index, 'ClusterCode']=birds.at[index, 'ClusterSize']
        birds.at[index, 'ClusterSize']=number

# investigate inputs (ClusterSize)
birds.loc[birds['ClusterSize']=='G'] # multiple
birds.loc[birds['ClusterSize']=='H'] # multiple
for letter in ['G', 'H']:
    rows = birds.loc[birds['ClusterSize']==letter].index.to_numpy()
    for index in rows:
        birds.at[index, 'ClusterSize']=1
        birds.at[index, 'ClusterCode']=letter

# change dtype (ClusterSize, Distance)
birds['ClusterSize'] = birds['ClusterSize'].astype('float64')
birds['Distance'] = birds['Distance'].astype('float64')

# make Y/N (Migrating, Visual)
birds = birds.fillna(value={'Migrating':0, 'Visual':0, 'ClusterSize':1, 'Sex':'U'})
birds['Visual'].replace('X', 1, inplace=True)
birds['Migrating'].replace('X', 1, inplace=True)

# delete empty lines
birds = birds.dropna(subset=['SpeciesCode'])
birds = birds.reset_index(drop=True) 

# fill in known nans (How, Minute, Distance, StartTime)
np.where(birds['How'].isnull())[0] # 600, 624, 676, 704, 777, 778, 1029, 1241, 1289
for number in [600, 624, 676, 704, 777, 778, 1029, 1241, 1289]:
    birds.at[number, 'How']='S'
np.where(birds['Minute'].isnull())[0] # 88s
np.where(birds['Distance'].isnull())[0] # 600, 624, 676, 1029, 1241, 1289
for number in [600, 624, 676, 1029, 1241, 1289]:
    birds.at[number, 'Distance']=round(birds['Distance'].mean(), 0)
for row in range(len(birds)):
    fillDown(birds, 'StartTime', row)

# fill in 88s
birds = birds.fillna(value={'StartTime':'00:00', 'Minute':88, 'Distance':round(birds['Distance'].mean(), 0)})

## FEATURE ENGINEERING

# normalize time
minutes = birds['StartTime'].apply(lambda x: str(x).split(':')[1]).astype(int)
hours = birds['StartTime'].apply(lambda x: str(x).split(':')[0]).astype(int)
minutes = minutes.apply(lambda x: round(x/60, 2))
birds['StartTime'] = hours+minutes

## EXPORT
birds.to_csv('E:\Share Drive\Farm Surveys\Raw Data\Spring 2020\countdata_cleaned.csv', index=False)


