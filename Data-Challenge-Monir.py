#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np


# In[4]:


# importing csv files to the repositery as data frames/ -Monir
Patients = pd.read_csv("Patients.csv")

Patients.head(10)


# In[5]:


# test patients with only 4 digit code
Test_patients = Patients.loc[Patients['PatientID'].astype(str).str.len() == 4]

# After removed test patients 
Patients = Patients.loc[Patients['PatientID'].astype(str).str.len() == 6]


# In[6]:


Patients.head(10)


# In[7]:


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


# In[8]:


# A new column is created called CHL
Appointments['CHL']="NA"


# In[9]:


Appointments.loc[(Appointments['Result'].astype(str).str.contains("Chlamydia", na=False, case=False) & Appointments['Result'].astype(str).str.contains("detected", na=False, case=False) & ~Appointments['Result'].astype(str).str.contains("not", na=False, case=False)), 'CHL'] = 1


# In[10]:


Appointments.loc[(Appointments['Result'].astype(str).str.contains("Chlamydia", na=False, case=False) & Appointments['Result'].astype(str).str.contains("detected", na=False, case=False) & Appointments['Result'].astype(str).str.contains("not", na=False, case=False)), 'CHL'] = 1


# In[11]:


Appointments.head(20)


# In[15]:


Patients_df = Patients.drop_duplicates(subset=['PatientID'])


# In[20]:


Appointments.dtypes


# In[21]:


Patients_df.dtypes


# In[33]:


Visits = pd.merge(Patients, Appointments, left_on='PatientID',right_on='Patient ID', how="left" )


# In[34]:


Visits.head(10) 


# In[35]:


Visits = Visits.drop(['Result','Patient ID'], axis=1)


# In[36]:


Visits.head(10) 


# In[39]:


Visits.rename(columns={"PatientID" : "SLK", "SiteID" : "Site", "ApptDate" : "VisitDate"}, inplace=True)


# In[40]:


Visits.head(10) 


# In[82]:


Visits_df=Visits


# In[69]:


import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("atlas.sqlite")

cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

table_name = cursor.fetchall()

print(table_name)


# In[70]:


cursor.execute('SELECT * FROM Visits;')
names = list(map(lambda x: x[0], cursor.description))

print(names)


# In[71]:


# The result of a "cursor.execute" can be iterated over by row
for row in cursor.execute('SELECT SLK, SiteID, VisitDate, AgeGroup, CHL FROM Visits group by SLK;'):
    print(row)


# In[72]:


# Load the data into a DataFrame
Visits_table = pd.read_sql_query("SELECT * from Visits", con)
Visits_table.head()


# In[83]:


columnsTitles = ['SLK', 'Site', 'VisitDate', 'AgeGroup', 'CHL']
Visits_df = Visits_df.reindex(columns=columnsTitles)
Visits_df.rename(columns={"Site" : "SiteID"}, inplace=True)
PatientAppointments = Visits_df
PatientAppointments.head()


# In[84]:


Visits_table.append(PatientAppointments, ignore_index = True)


# In[85]:


# Write the new DataFrame to SQLite table
Visits_table.to_sql("Visits", con, if_exists="replace")


# In[ ]:




