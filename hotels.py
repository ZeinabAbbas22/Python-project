#here i will import the data from the xcel file named hotels, i should improt  all rows
import pandas as pd
hotels = pd.read_excel('hotels.xlsx')
pd.set_option('display.max_rows',None)
print('The Data in Hotels excel file are :')
print(hotels)
#done

