# Data_Challenge

# 1. Fetch and Clean the data using Python-Pandas
### 1.1 Fetch all 8,891 datasets from PUBLIC_DISPATCHSCADA data.

**For PUBLIC_DISPATCHSCADA data 8,891 files are extracted in a single folder** 

Python-Pandas necessary code for fetching the data from PUBLIC_DISPATCHSCADA data

```python
# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np

# importing csv files to the repositery as data frames/ -Monir
Patients = pd.read_csv("Patients.csv")
```
**PUBLIC_DISPATCHSCADA_df contains 3,326,960 rows × 6 columns**

![DISPATCHSCADA](Images/DISPATCHSCADA-dataframe.png?raw=true "DISPATCHSCADA")

### 1.2 Fetch 1,674 datasets from PUBLIC_TRADINGIS data.

**Similarly For PUBLIC_TRADINGIS data 1,674 files are extracted in a single folder** 

```python
# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np
from csv import reader

# assign dataset names - Monir
PUBLIC_TRADINGIS_list_of_files = []

#read all dataset names with starting PUBLIC_DISPATCHSCADA - Monir
PUBLIC_TRADINGIS_list_of_files = glob.glob('PUBLIC_TRADINGIS*.csv')

# create empty list
dataframes_list = []

list_of_names = PUBLIC_TRADINGIS_list_of_files

# append datasets into teh list
for i in range(len(list_of_names)):
    # read csv file as a list of lists
    with open(list_of_names[i], 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        #print(list_of_rows)
        #temp_df = pd.DataFrame(list_of_rows)
        temp_df = pd.DataFrame(list_of_rows[9:14])
    dataframes_list.append(temp_df)
    list_of_column = list_of_rows[8]
    
    
    #temp_df = pd.read_csv(list_of_names[i], skiprows = 1, skipfooter = 1)
    #dataframes_list[i]=temp_df
    #dataframes_list.append(temp_df)
    
```

![TradingIS](Images/Trading-dataframe.png?raw=true "TradingIS")
