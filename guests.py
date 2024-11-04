#here i will import the data from the xcel file named guests, it should improt  all rows
import pandas as pd
guests = pd.read_excel('guests.xlsx')
pd.set_option('display.max_rows',None)
print('The Data in Guests excel file are :')
print(guests)
#done