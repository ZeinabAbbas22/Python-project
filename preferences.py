#here i will import the data from the xcel file named prefereneces, it should improt  all rows
import pandas as pd
prefereneces = pd.read_excel('preferences.xlsx')
pd.set_option('display.max_rows',None)
print('The Data in Preferences excel file are :')
print(prefereneces)
#done
