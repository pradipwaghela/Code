import pandas as pd
import numpy as np

file = open('log_file.txt','r')
s= file.read()
lines = s.split('\n')

filt_lines =[]
for l in lines:
    if l.startswith('$'):
        filt_lines.append(l)

array = [l.split() for l in filt_lines]

log_df = pd.DataFrame(array)
print(log_df)
# And write it to csv
log_df.to_csv("log2.csv",header=["Start Character","Header","Vendor Identification"	,"Software Version","PACKET TYPE","PACKET IDENTIFIER","Live /History Packet","IMEI Number","Vehicle Registration Number","GPS Fix.1 or 0","Date in DDMMYYYY Format"	,"Time HHMMSS Format","Latitude in decimal degree & Direction",	"Longitude in decimal degree & Direction","Speed","Heading","Number Of Satellites","Altitude in meters","PDOP Positional dilution of precision","HDOP Horizontal dilution of precision"	,"Network Operator Name","Ignition Status","Vehicle Battery Status (1 or 0)","Vehicle Battery Voltage",	"Internal Battery Voltage",	"Emergency Status (1 or 0)","Tamper Alert. C (Close) or O (Open)","GSM Signal Strength"	,"MCC",	"MNC","LAC"	,"Cell ID","NMR (Network Measurement Report) Neighboring Cell IDs","NA","NA","NA","NA","NA"],index=False)

"""
Start Character	= Col 0
Header	= Col 1
Vendor Identification = Col 2
Software Version	= Col 3
PACKET TYPE	= col 4
PACKET IDENTIFIER	= col 24
Live /History Packet	= col 5 
IMEI Number	= col 6
Vehicle Registration Number	= col 7
GPS Fix.1 or 0	= col 8
Date in DDMMYYYY Format	= col 9 
Time HHMMSS Format	= col 10
Latitude in = col 11
decimal degree & Direction	= col 12
Longitude in  = col 13
decimal degree & Direction		= col 14
Speed	= col 15
Heading	= col 16
Number Of Satellites = col 17
Altitude in meters	= col 18
PDOP = col 19
Positional dilution of precision	col 20
HDOP Horizontal dilution of precision	
Network Operator Name	= col 21
Ignition Status	
Vehicle Battery Status (1 or 0)	
Vehicle Battery Voltage	
Internal Battery Voltage	
Emergency Status (1 or 0)	
Tamper Alert. C (Close) or O (Open)	
GSM Signal Strength	"Start Character","Header",	"Vendor Identification"	,"Software Version',	"PACKET TYPE"	,"PACKET IDENTIFIER"	,"Live /History Packet"	,"IMEI Number"	,"Vehicle Registration Number"	,"GPS Fix.1 or 0"	,"Date in DDMMYYYY Format"	,"Time HHMMSS Format",	"Latitude in decimal degree & Direction",		"Longitude in decimal degree & Direction",		"Speed"	,"Heading"	,"Number Of Satellites"	,"Altitude in meters"	,"PDOP Positional dilution of precision",	"HDOP Horizontal dilution of precision"	,"Network Operator Name",	"Ignition Status",	"Vehicle Battery Status (1 or 0)",	"Vehicle Battery Voltage",	"Internal Battery Voltage",	"Emergency Status (1 or 0)",	"Tamper Alert. C (Close) or O (Open)"	,"GSM Signal Strength"	,"MCC",	"MNC"	,"LAC"	,"Cell ID","	NMR (Network Measurement Report) Neighboring Cell IDs"
Cell ID	
NMR (Network Measurement Report) Neighboring Cell IDs		

"""
"""
"Start Character","Header",	"Vendor Identification"	,"Software Version',	"PACKET TYPE"	,"PACKET IDENTIFIER"	,"Live /History Packet"	,"IMEI Number"	,"Vehicle Registration Number"	,"GPS Fix.1 or 0"	,"Date in DDMMYYYY Format"	,"Time HHMMSS Format",	"Latitude in decimal degree & Direction",		"Longitude in decimal degree & Direction",		"Speed"	,"Heading"	,"Number Of Satellites"	,"Altitude in meters"	,"PDOP Positional dilution of precision",	"HDOP Horizontal dilution of precision"	,"Network Operator Name",	"Ignition Status",	"Vehicle Battery Status (1 or 0)",	"Vehicle Battery Voltage",	"Internal Battery Voltage",	"Emergency Status (1 or 0)",	"Tamper Alert. C (Close) or O (Open)"	,"GSM Signal Strength"	,"MCC",	"MNC"	,"LAC"	,"Cell ID","	NMR (Network Measurement Report) Neighboring Cell IDs"

"""