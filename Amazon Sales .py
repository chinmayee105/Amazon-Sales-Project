#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('Amazon Sale Report.csv')


# In[3]:


df.shape


# In[4]:


df.head(5)


# In[78]:


df.tail(5)


# In[79]:


df.info()


# In[80]:


# Block Unrelated/Blank Columns

df.drop(['New','PendingS'], axis=1, inplace=True)


# In[81]:


df.info()


# In[82]:


# Check the Null values

pd.isnull(df)


# In[83]:


# Sum wil give total values of null values

pd.isnull(df).sum()


# In[84]:


df.shape


# In[85]:


df.columns


# In[86]:


# Change Data Type
df[ 'ship-postal-code' ]=df[ 'ship-postal-code' ].astype('float')


# In[87]:


df['ship-postal-code'].dtype


# In[88]:


df['Date']=pd.to_datetime(df[ 'Date' ])


# In[89]:


df.info()


# In[90]:


df.columns


# In[91]:


# Rename Columns
df.rename(columns={'Qty':'Quantity'})


# In[92]:


df.describe(include='object')


# In[93]:


# Use describe() for specific columns
df[['Qty','Amount']].describe()


# ## Exploratory Data Analysis

# In[94]:


df.columns


# ### * Size

# In[95]:


ax = sns.countplot(x='Size',data=df)


# ### * Group By

# #### The GroupBy() function in pandas is used to group data based on 1 or more columns in a Dataframe

# In[98]:


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[99]:


S_Qty=df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

sns.barplot(x='Size',y='Qty',data=S_Qty)


# ###### From above Graph you can see that most of the Qty buys M-size in the sales

# ### * Courier Status

# In[100]:


sns.countplot(data=df, x='Courier Status', hue= 'Status')


# In[101]:


plt.figure(figsize=(10,5))
ax = sns.countplot(data=df, x='Courier Status', hue='Status')
plt.show()


# ###### From Above Graph the majorityof the orders are shipped through the courier

# In[102]:


# Histogram

df['Size'].hist()


# In[103]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize = (10,5))
plt.hist(column_data, bins=20, edgecolor='Yellow')
plt.xticks(rotation=90)
plt.show()


# ###### From above Graph you can see that most of the buyers are T-Shirt

# In[107]:


# Checking B2B Data by using pie chart

B2B_Check = df['B2B'].value_counts()

# Plot the pie chart

plt.pie(B2B_Check, labels=B2B_Check.index, autopct = '%1.1f%%')

# plt.axis('Equal')

plt.show()


# ###### From above chart we can see that maximum i.e. 99.3% of buyers are retailers and 0.7% are B2B buyers

# ### Category and Size the products

# In[109]:


# Prepare data for Scatter Plot
x_data = df['Category']
y_data = df['Size']

# Plot the Scatter Plot
plt.scatter(x_data,y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.xticks(rotation=90)
plt.show()


# ### Which city or state buy the most of the products

# In[110]:


plt.figure(figsize=(12,6))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[115]:


# Top 10_states
top_10_state = df['ship-state'].value_counts().head(10)

# Plot count of cities by state

plt.figure(figsize=(12,6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=45)
plt.show()


# ###### From above Graph you can see that most of the buyers are Maharastra State

# ## -- Conclusion

# ###### The Data Analysis reveals that the business has a significant customers base in Maharastra State, mainly serves retailers, orders through Amazon, experiences high demand for T-shirt, and sees M-Size as the preferred choice among buyers.

# In[ ]:




