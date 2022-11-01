
# # importing the pandas library
# import pandas as pd
  
# # reading the csv file
# df = pd.read_csv("AllDetails.csv")
  
# # updating the column value/data
# df.loc[5, 'Name'] = 'SHIV CHANDRA'
  
# # writing into the file
# df.to_csv("AllDetails.csv", index=False)
  
# print(df)

#-------------------------------------------------------------

# import csv

# op = open("AllDetails.csv","r")
# dt = csv.DictReader(op)
# print(dt)
# for r in dt:
#     print(r)
#-------------------------------------------------------------


# print('both tables')
# df = pd.read_csv("data.csv")
# df.to_csv("data.csv", index=False)
# print(df)
# print(' ')
# df = pd.read_csv("AllDetails.csv")
# df.to_csv("AllDetails.csv", index=False)
# print(df)
# print('#---------------------------------------------------------------------------')

# reading the csv file
df = pd.read_csv("data.csv")
  
# updating the column value/data
#df['Status'] = df.where(df['Status'].isna(),df['Status'].replace('A'))
df2 = df['INDUSTRYID'] = df['INDUSTRYID'].replace(to_replace="NaN", value='3.0')
  
# writing into the file
df2.to_csv("data2.csv", index=False)
  
print(df2)
print('#---------------------------------------------------------------------------')

#---------------------------------------------------------------------------

# df = pd.read_csv("AllDetails.csv")
  
# # updating the column value/data
# #df['Status'] = df.where(df['Status'].isna(),df['Status'].replace('A'))

# df['Name'] = df['Name'].replace( {None : 'A'})
  
# # writing into the file
# df.to_csv("AllDetails.csv", index=False)
  
# print(df)