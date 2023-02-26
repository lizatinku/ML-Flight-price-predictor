#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


dataset = pd.read_csv("economy.csv")
dataset.head()


# In[4]:


dataset.isnull().sum()


# In[5]:


dataset["journey_day"] = pd.to_datetime(dataset.date, format="%d-%m-%Y").dt.day
dataset["journey_month"] = pd.to_datetime(dataset["date"], format = "%d-%m-%Y").dt.month
dataset.head()


# In[6]:


dataset.drop(["date"], axis = 1, inplace = True)
dataset.head()


# In[7]:


# Extracting Hours
dataset["dep_hour"] = pd.to_datetime(dataset["dep_time"]).dt.hour
dataset["dep_min"] = pd.to_datetime(dataset["dep_time"]).dt.minute
dataset.drop(["dep_time"], axis = 1, inplace = True)
dataset.head()


# In[8]:


dataset["arrival_hour"] = pd.to_datetime(dataset["arr_time"]).dt.hour
dataset["arrival_min"] = pd.to_datetime(dataset["arr_time"]).dt.minute
dataset.drop(["arr_time"], axis = 1, inplace = True)
dataset.head()


# In[9]:


duration = list(dataset["time_taken"])


# In[10]:
# BUG HAS BEEN FIXED FROM HERE ON OUT

for i in range(len(duration)):
    if len(duration[i].split()) != 2:    # Check if duration contains only hour or mins
        if "h" in duration[i]:
            duration[i] = duration[i].strip() + " 0m"   # Adds 0 minute
        else:
            duration[i] = "0h " + duration[i] # Adds 0 hour
dataset.head()


# In[19]:


duration_hours = []
duration_mins = []

for i in range(len(duration)):
    if((duration[i]=='1.03h m') or (duration[i]=='1.02h m')or (duration[i]=='1.01h m')):
        if((duration[i]=='1.03h m')): 
            duration_hours.append(1)
            duration_mins.append(3)
        elif (duration[i]=='1.02h m'):
            duration_hours.append(1)
            duration_mins.append(2)
        elif (duration[i]=='1.01h m'):
            duration_hours.append(1)
            duration_mins.append(3)
    else:
        duration_hours.append(int(duration[i].split(sep = "h")[0]))    # Extract hours from duration
        duration_mins.append(int(duration[i].split(sep = "m")[0].split()[-1]))

# Extracts only minutes from duration
# Add duration_hours and duration_mins list to our dataset df
dataset["Duration_hours"] = duration_hours
dataset["Duration_mins"] = duration_mins
# Drop Duration column from the dataset
dataset.drop(["time_taken"], axis = 1, inplace = True)

dataset.head()


# In[21]:


dataset["airline"].value_counts()


# In[23]:


Airline = dataset[["airline"]]
Current_Airline_List = Airline['airline']
New_Airline_List = []
for carrier in Current_Airline_List:
    if carrier in ['GO FIRST', 'Indigo', 'Air India', 'SpiceJet',
       'Trujet', 'StarAir', 'Vistara', 'AirAsia']:
        New_Airline_List.append(carrier)
    else:
        New_Airline_List.append('Other')
Airline['airline'] = pd.DataFrame(New_Airline_List)
Airline['airline'].value_counts()


# In[24]:


# Feature engineering on: Source
print(dataset["from"].value_counts())
# As Source is Nominal Categorical data we will perform OneHotEncoding
Source = dataset[["from"]]
Source = pd.get_dummies(Source, drop_first= True) 
# drop_first= True means we drop the first column to prevent multicollinearity
Source.head()


# In[25]:


# Feature engineering on: Destination
print(dataset["to"].value_counts())
# Renaming destination 'New Delhi' to 'Delhi' - to match with Source
Destination = dataset[["to"]]
Current_Destination_List = Destination['to']
New_Destination_List = []
for value in Current_Destination_List:
    if value in ['New Delhi']:
        New_Destination_List.append('Delhi')
    else:
        New_Destination_List.append(value)
Destination['to'] = pd.DataFrame(New_Destination_List)

# As Destination is Nominal Categorical data we will perform OneHotEncoding
Destination = pd.get_dummies(Destination, drop_first = True)
Destination.head()


# In[ ]:




