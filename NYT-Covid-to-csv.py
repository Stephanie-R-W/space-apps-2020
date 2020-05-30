# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:05:39 2020

@author: mmcginnes
"""

import pandas as pd
from datetime import date 
filelocation = 'C:/Users/mmcginnes/Documents/Temp/' #where the output will be written. 
#We are only interested in the DMV Area, so filter down to those states.
states = ['Virginia','Maryland','District of Columbia']
df=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
print(df.head())
df = df[df['state'].isin(states)]
#The NYT only provides totals for each day by county. To get the
#Number of new cases, Sort by State/county using the FIPS codes


df.sort_values(by=['fips','state','county','date'], inplace=True)

#then calculate the difference between the current row and the previous row
#if they are the same county. Counts go into an array.
#'Unknown' counties are causing some problems. Probably need to give them
#their state level fips code (state code +000)
newcases = []
for row in range(0,len(df)):
    if row == 0:
       newcases.append(df.iloc[row]['cases'])
    elif df.iloc[row]['fips'] == df.iloc[row-1]['fips']:
        newcases.append (df.iloc[row]['cases']-df.iloc[row-1]['cases'])
    else:
        newcases.append(df.iloc[row]['cases'])
#New cases array gets added as a column to the dataframe (df)    
df['new cases'] = newcases
#Repete for deaths     
newdeaths = []
for row in range(0,len(df)):
    if row == 0:
       newdeaths.append(df.iloc[row]['deaths'])
    elif df.iloc[row]['fips'] == df.iloc[row-1]['fips']:
        newdeaths.append (df.iloc[row]['deaths']-df.iloc[row-1]['deaths'])
    else:
        newdeaths.append(df.iloc[row]['deaths'])

 
df['new deaths'] = newdeaths
#write it all to a CSV so it can be imported into Tableau.
df.to_csv(filelocation+'NYTCovid19.csv', index=False)
print(df.tail())
print(date.today())

#for row in range(len(df2)):
#    print (df2.iloc[row],['New cases'])
