#I will work on this file on the random allocation
import pandas as pd
hotels = pd.read_excel('data/hotels.xlsx')
guests = pd.read_excel('data/guests.xlsx')
preferences = pd.read_excel('data/preferences.xlsx')


print("Hotels prova Data:")
print(hotels.head())
print("\nGuests prova Data:")
print(guests.head())
print("\nPreferences prova Data:")
print(preferences.head())

#this printed only 4 rows for each of the 3 files


#Checking if data and info in rows are applicable and whethetr there is null rows  
print("Hotels Dataset Info:")
print(hotels.info())

print("\nGuests Dataset Info:")
print(guests.info())

print("\nPreferences Dataset Info:")
print(preferences.info())

import random

#i must insert columns that check for rooms available and then the returns of bookings
print("Columns in Hotels DataFrame:", hotels.columns)
hotels['vacant_rooms'] = hotels['rooms']  # Set initial vacant rooms
hotels['earnings'] = 0.0  # Initialize earnings to 0 for each hotel

print("Updated Hotels DataFrame:")
print(hotels.head())

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


print("Full Hotels DataFrame:")
print(hotels)
 




