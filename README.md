# Data_Challenge

```python
# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np
```
**1. Read Patients.csv into memory in an object called Patients**

```python
# importing csv files to the repositery as data frames/ -Monir
Patients = pd.read_csv("Patients.csv")

Patients.head()
```
```sql
PatientID	Site	AgeGroup
0	866951	K	15-19
1	120640	C	50+
2	358689	K	50+
3	295376	Y	40-49
4	211916	L	25-29
```
**2. Patients has a column called PatientID which contains 6 digit code for patients except for a few test
patients with only 4 digit code. Identify these test patients with 4 digit PatientID and remove these
rows.**

```python

# test patients with only 4 digit code
Test_patients = Patients.loc[Patients['PatientID'].astype(str).str.len() == 4]

# After removed test patients 
Patients = Patients.loc[Patients['PatientID'].astype(str).str.len() == 6]

```
**3. Read Appointments_2019.csv, Appointments_2020.csv and Appointments_20201.csv into memory
and append together into an object called Appointments**

```python

# assign dataset names - Monir
list_of_files = []

# all dataset names with starting Appointments - Monir
list_of_files = glob.glob('Appointments*.csv')

# all dataset names with starting Appointments - Monir
list_of_files = glob.glob('Appointments*.csv')

# create empty list
dataframes_list = []

# append datasets into teh list
for i in range(len(list_of_files)):
    temp_df = pd.read_csv(list_of_files[i])
    dataframes_list.append(temp_df)


Appointments = pd.concat(dataframes_list)

Appointments.head()
```
```sql
	Patient ID	ApptDate	Result
0	284414	30/12/2019	*NOT DETECTED CHLAMYDIA
1	720514	8/09/2019	SYPHILIS ***DETECTED***
2	144037	26/01/2019	301 chlamydia ***NOT DETECTED*** 301 301
3	906764	17/06/2019	*NOT DETECTED CHLAMYDIA
4	391327	12/06/2019	chlamydia not detected

```

**4. Appointments also has a column called Result which contains the terms “Chlamydia” and “detected”
or “not detected”. Create a new column called CHL which which value is equal to 1 if the words
“Chlamydia” and “detected” is in Result, 0 if “Chlamydia” and “not detected” is in Result, and NA
otherwise.**

```python

Appointments.loc[(Appointments['Result'].astype(str).str.contains("Chlamydia") & Appointments['Result'].astype(str).str.contains("detected")), 'CHL'] = 1


```

**5. Left join the Appointments data frame to Patients data frame using the keys PatientID in Patients
and Patient ID in Appointments. Assign this joined data to object called Visits.**

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
