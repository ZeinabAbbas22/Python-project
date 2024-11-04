#trying the code 

import pandas as pd

# Update the paths to include the 'data' folder
hotels = pd.read_excel('data/hotels.xlsx')
guests = pd.read_excel('data/guests.xlsx')
preferences = pd.read_excel('data/preferences.xlsx')

print("Hotels Data:")
print(hotels.head())
print("\nGuests Data:")
print(guests.head())
print("\nPreferences Data:")
print(preferences.head())

# Checking if data and info whether its all good 
print("Hotels Dataset Info:")
print(hotels.info())

print("\nGuests Dataset Info:")
print(guests.info())

print("\nPreferences Dataset Info:")
print(preferences.info())

#taking my data to right place
import pandas as pd

hotels = pd.read_excel('data/hotels.xlsx') 

print(hotels.columns)  


hotels.columns = hotels.columns.str.strip()  
availabilityinitial = hotels[hotels['rooms'] > 0]  

output = 'outcomes/availabilityinitial.xlsx'

availabilityinitial.to_excel(output, index=False)
print(f"Filtered available hotels saved to {output}.")

#random allocation 

print("Guests Data:")
print(guests.head())
#checked
import random

allocations = []  
#the equation
for index, guest in guests.iterrows():
    chosen_hotel = random.choice(availabilityinitial['hotel'].tolist())
    allocations.append({'guest': guest['guest'], 'allocated_hotel': chosen_hotel})

allocation_df = pd.DataFrame(allocations)

#see final result on the other excel file so we add this function 
output = 'outcomes/random_allocations.xlsx'

# Save the allocations DataFrame to an Excel file
allocation_df.to_excel(output, index=False)
print(f"Guest allocations saved to {output}.")

# now i want to have this results moved to also an excel file under the folder of outcomes

 


