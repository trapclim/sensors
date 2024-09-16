#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:27:51 2023

@author: jurad
"""
import pandas as pd


def get_egg_data(ID,start,end,variable,res): #takes strings, dates in SO-8601 format. res in "30M" or "1H"
    """ Function takes 5 arguments, all are strings except variable, which is a list. 
    Start and end dates are in ISO-8601 format. Variable is a list of strings of
    provided variable names. Res gives averaged data intervals in the format 
    of (minutes)M or (hours)M e.g. 30M or 1H Returns data frame of selected 
    variables over selected time at selected resultion intervals. Prints out 
    coordinates of station and average elevation. Coordinates and elevation can be 
    included as time series if the station is moving.
    """
    ID = str(ID)
    start = str(start)
    start = start.replace(":","%3A")
    end = str(end)
    end = end.replace(":","%3A")
    res = str(res)
    res = "PT"+ res

    url = "https://airqualityegg.com/api/v2/messages/device/"+ID+"?apiKey=6NWX5NP-47TMNGN-K1PHKWE-8KMS56G&format=csv&start-date="+start+"&end-date="+end+"&resolution="+res+"&reduced=1"
    print(url)
    df = pd.read_csv(url)
    
    alt = df["altitude[m]"].mean()
    
    lat = df['latitude[deg]'].values[1]
    lon = df['longitude[deg]'].values[1]
    
    collist = df.columns.values.tolist()
    delcol = list([])
    for x in collist: #for each in the dataframe
        
        if x not in variable: #if it appears in the wanted variable list
            
            delcol.append(x) #append it to the delete list
    for x in delcol:
        
        df = df.drop(x, axis=1)#keep all df columns that are in that list
    
    print("Latitude[deg] is:")
    print(lat)
    print("Longitude[deg] is:")
    print(lon)
    print("altitude[m] is:")
    print (alt)
    return df
    
#INPUT EXAMPLE

variable = list(["time","temperature[degC]","humidity[percent]","pressure[Pa]",
                "co2[ppm]","pm10p0[ug/m^3]","pm2p5[ug/m^3]","pm1p0[ug/m^3]"])

df = get_egg_data("egg00802e8e050b0111","2023-03-01T00:00:00.000Z","2023-03-02T00:00:00.000Z",variable,"1H")

#df.to_csv('file_name.csv', index=False,float_format='%.2f')




#get help converting variable list to kwargs
#make read me with once done and approved
#Include all variable names and table of all eggs and serial numbers