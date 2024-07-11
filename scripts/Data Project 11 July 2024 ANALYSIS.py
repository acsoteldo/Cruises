#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv(r"cruise_dataset CLEANED.csv")

data.head()
data.dtypes


# In[2]:


data['Emissions'] = data['Tonnage'] * 0.4 + data['Passengers'] * 0.2
data['Fuel_consumption'] = data['Tonnage'] * 0.5 + data['Passengers'] * 0.3

data.head()


# In[3]:


df = pd.DataFrame(data)

# Regression for Fuel Consumption
X = df[['Tonnage', 'Passengers']]
y = df['Fuel_consumption']
X = sm.add_constant(X)  # Adds a constant term to the predictor
model = sm.OLS(y, X).fit()
print(model.summary())

# Regression for Emissions
y = df['Emissions']
model = sm.OLS(y, X).fit()
print(model.summary())


# In[4]:


# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting Tonnage vs. Crew
plt.figure(figsize=(8, 6))
plt.scatter(df['Tonnage'], df['Crew'], alpha=0.5)
plt.title('Tonnage vs. Crew')
plt.xlabel('Tonnage')
plt.ylabel('Crew')
plt.grid(True)
plt.show()


# In[5]:


##Discuss how ship size (tonnage) influences crew requirements. Larger ships typically require more crew to operate efficiently.


# In[6]:


# Plotting Passenger Density vs. Emissions
plt.figure(figsize=(8, 6))
plt.scatter(df['Passenger_density'], df['Emissions'], alpha=0.5)
plt.title('Passenger Density vs. Emissions')
plt.xlabel('Passenger Density')
plt.ylabel('Emissions')
plt.grid(True)
plt.show()


# In[7]:


##Explore the relationship between passenger density and emissions. Higher passenger density can lead to increased emissions per passenger mile traveled.


# In[8]:


# Plotting Age vs. Fuel Consumption
plt.figure(figsize=(8, 6))
plt.bar(df['Age'], df['Fuel_consumption'])
plt.title('Age vs. Fuel Consumption')
plt.xlabel('Age')
plt.ylabel('Fuel Consumption')
plt.grid(True)
plt.show()


# In[9]:


##Analyze how the age of a ship impacts fuel consumption. Older ships may have outdated technologies that contribute to higher fuel consumption rates.

