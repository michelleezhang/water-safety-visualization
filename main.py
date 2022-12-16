import pandas as pd
# this reads our txt file, using '  ' as the separation
all_data = pd.read_csv('data/UCMR4_All.txt', sep='	', header=None, low_memory=False)
zipcode_data = pd.read_csv('data/UCMR4_ZipCodes.txt', sep='	', header=None)

input_zipcode = '60201'

result_set = set() # empty set

# convert zipcode to PWSID
for i in range(len(zipcode_data)):
    if zipcode_data.loc[i,1] == input_zipcode:
        input_PWSID = zipcode_data.loc[i,0]

# find desired row in data
for j in range(len(all_data)):
    if input_PWSID == all_data.loc[j,0]: 
        # for some reason, PWSID's type in the data table is "pandas series", so we convert to string here
        selected_row = all_data.loc[j,:]
        result_set.add(selected_row[13])
        # OFTEN HAS MULTIPLE ROWS
print(result_set)



