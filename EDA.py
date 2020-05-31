# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

## IMPORT DATA
data = pd.read_csv("Spring2020.csv")
codes = pd.read_csv("SpeciesCodes.csv")

data.columns
data.head()

## CLEAN DATA
# clean up false NAs
data = data.dropna(subset=['SpeciesCode'])
data = data.fillna(value={'Visual':0, 'Sex':'U', 'Migrating':0,'ClusterSize':1})
data['Visual'].replace('X', 1, inplace=True)

# NA report
total_na = data.isna().sum().sort_values(ascending=False)
percent_na = (data.isna().sum()*100/len(data)).sort_values(ascending=False)
data_na = pd.concat([total_na, percent_na], axis=1, keys=['Total', 'Percent'])

# make time numeric

# investigate problematic NAs

# add species names

## EXPLORATORY PLOTS
# abundance plot
abun = data.SpeciesCode.value_counts()
ax,f = plt.subplots(figsize=(16,10))
sns.barplot(x=abun.index, y=abun)
plt.yticks(np.arange(0,100,10))
plt.xticks(rotation=90)
plt.ylabel("Abundance")
plt.xlabel("Species")

# distance plot
dist = data.Distance
ax,f = plt.subplots(figsize=(16,10))
sns.distplot(dist)
plt.xticks(np.arange(0,1225,25), rotation=90)

# species by distance plot
dist_grouped = data.groupby('SpeciesCode', as_index=False)['Distance'].mean()
sorted_index = dist_grouped.sort_values(by=['Distance'], axis=0, ascending=False).index
data_sorted=dist_grouped.reindex(sorted_index)
data_sorted=data_sorted.reindex(sorted_index)
ax,f = plt.subplots(figsize=(16,10))
sns.barplot(x=data_sorted.SpeciesCode, y=data_sorted.Distance)
plt.xticks(rotation=90)
plt.yticks(np.arange(0,1050,50))
plt.ylabel("Distance (mean)")
plt.xlabel("Species")
