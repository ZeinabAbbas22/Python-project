import pandas as pd

hotels = pd.read_excel('hotels.xlsx')
guests = pd.read_excel('guests.xlsx')
preferences = pd.read_excel('preferences.xlsx')

print("Hotels Data:")
print(hotels.head())
print("\nGuests Data:")
print(guests.head())
print("\nPreferences Data:")
print(preferences.head())
