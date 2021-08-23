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
```
1. Read Patients.csv into memory in an object called Patients

```python
# importing csv files to the repositery as data frames/ -Monir
Patients = pd.read_csv("Patients.csv")

Patients.head()

PatientID	Site	AgeGroup
0	866951	K	15-19
1	120640	C	50+
2	358689	K	50+
3	295376	Y	40-49
4	211916	L	25-29
```
2. Patients has a column called PatientID which contains 6 digit code for patients except for a few test
patients with only 4 digit code. Identify these test patients with 4 digit PatientID and remove these
rows.

```python

# test patients with only 4 digit code
Test_patients = Patients.loc[Patients['PatientID'].astype(str).str.len() == 4]

# After removed test patients 
Patients = Patients.loc[Patients['PatientID'].astype(str).str.len() == 6]

```
3. Read Appointments_2019.csv, Appointments_2020.csv and Appointments_20201.csv into memory
and append together into an object called Appointments

```python



```

4. Appointments also has a column called Result which contains the terms “Chlamydia” and “detected”
or “not detected”. Create a new column called CHL which which value is equal to 1 if the words
“Chlamydia” and “detected” is in Result, 0 if “Chlamydia” and “not detected” is in Result, and NA
otherwise.

```python

Here....

```

5. Left join the Appointments data frame to Patients data frame using the keys PatientID in Patients
and Patient ID in Appointments. Assign this joined data to object called Visits.

```python

Here....

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
