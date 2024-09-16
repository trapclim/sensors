#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:04:31 2023

@author: jurad
"""

# Egg Data API Function#


`def get_egg_data(ID,start,end,variable,res):`

This egg data API function outputs a dataframe of containing all selected 
variables from the indicated sensor. All arguments are strings except for 
"variable", which is a list of strings. Function also returns the 1st results
of latitude and longitude coordinates of the selected timeframe, as well as the
mean altitude of the entire timeframe. These strings are placed into a url
which webscrapes data from this link:

https://airqualityegg.com/api-docs/


##Valid "variable" Names##

An example of all valid variable names for air quality egg sensors is as follows:


`variable = list(["time","temperature[degC]","humidity[percent]","pressure[Pa]",`
                `"co2[ppm]","pm10p0[ug/m^3]","pm2p5[ug/m^3]","pm1p0[ug/m^3]",`
               ` "latitude[deg]", "longitude[deg]", "altitude[m]"])`
               
An example of all valid variable names for soil moisture sensors is as follows:


`variable = list(['battery[V]','soilmoisture[percent]']`


## Valid "start" and "end" format##

Start and end dates are in ISO-8601 format such as:

"2023-03-20T00:00:00.000Z"


If there is no data in the indicated range, the code may respond with an altitude error or "service unavailable"



##Valide "res" arguments##

All res arguments take the form o:

"1H" for an hour
"30M" for 30 minutes

Other values such as as "60M" or "24H" or ".5H" can be used.

## Sensor Information##

The information on current sensor serial number, nickname, and variables are 
written in the following order:

* Serial Number

* Nickname

* Measures



egg00802e8e019b0111

SciFri_egg3_inTank_i

co2, pm2p5, pm10p0, pm1p0, temperature, humidity, pressure, latitude, longitude, altitude


egg00802e8e050b0111

Island Fitness (ITH)

co2, pm2p5, pm10p0, pm1p0, temperature, humidity, pressure, latitude, longitude, altitude


egg008042c13f980113

Cayuga Nature Center

co2, pm2p5, pm10p0, pm1p0, temperature, humidity, pressure, latitude, longitude, altitude


egg0080442c4cab0123

CHES_Egg_In_Tank (123)

co2, pm2p5, pm10p0, pm1p0, temperature, humidity, pressure, latitude, longitude, altitude


egg008044e767090121

Garage_Egg_CHES_lab

co2, pm2p5, pm10p0, pm1p0, temperature, humidity, pressure, latitude, longitude, altitude


eggccc0790000ee7c23

PLUGS

soiilmoisture, battery


eggccc0790000ee7c28

BALOO

soiilmoisture, battery


eggccc0790000ee7c2c

GLAMS

soiilmoisture, battery


eggccc0790000ee7c34

WIRER

soiilmoisture, battery


eggccc0790000ee7c44

TUMPY

soiilmoisture, battery


eggccc0790000ee7c46

REFIX

soiilmoisture, battery


eggccc0790000ee7c64

BENGA

soiilmoisture, battery


eggccc0790000ee7c69

PROST

soiilmoisture, battery


eggccc0790000ee7c6d

FENDY

soiilmoisture, battery


eggccc0790000ee7c75

ACINI

soiilmoisture, battery


eggccc0790000ee7c81

LUBRA

soiilmoisture, battery


eggccc0790000ee7c85

RUMEN

soiilmoisture, battery


eggccc0790000ee7e18

SHAPE

soiilmoisture, battery


eggccc0790000ee7e3d

BOBAS

soiilmoisture, battery

