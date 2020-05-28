# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:53:22 2020

@author: Work Station
"""

import pandas as pd

with open('text.txt', 'r') as f:
    species = f.readlines()

df = pd.DataFrame(species, columns=['All'])

df = df[df['All'] != ' ENGLISH NAME 4-LETTER CODE SCIENTIFIC NAME 6-LETTER CODE\n']
df.reset_index(drop=True, inplace=True)
df['All'] = df['All'].apply(lambda x: x.replace('*','').replace('\n',''))
df['SpeciesName'] = df['All'].apply(lambda x: x.split(' ')[0:-3])
for i in reversed(range(len(df.SpeciesName))):
    if '+' in df['SpeciesName'][i]:
        df = df.drop(df.index[i])
    else:
        pass
df.reset_index(drop=True, inplace=True)
df['SpeciesName'] = df['SpeciesName'].apply(lambda x: ' '.join(x))
df['FirstName'] = df['SpeciesName'].apply(lambda x: x.split(' ')[0])
df['SecondName'] = df['SpeciesName'].apply(lambda x: x.split(' ')[1])
df['4-LetterCode'] = df['SpeciesName'].apply(lambda x: x.split(' ')[-1])
for i in range(len(df.FirstName)):
    if df['SecondName'][i] == df['4-LetterCode'][i]:
        df['SecondName'][i] = df['FirstName'][i]
        df['FirstName'][i] = 'NA'
    else:
        pass
df.drop('All', axis=1, inplace=True)
df.drop('SpeciesName', axis=1, inplace=True)
df.to_csv('SpeciesCodes.csv', index=False)


