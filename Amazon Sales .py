
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

df = pd.read_csv('Amazon Sale Report.csv')

df.shape

df.head(5)

df.tail(5)

df.info()


# Block Unrelated/Blank Columns

df.drop(['New','PendingS'], axis=1, inplace=True)

df.info()

---------------------------------------------------------------------------------------------------------------------------------------------------
# Check the Null values

pd.isnull(df)

---------------------------------------------------------------------------------------------------------------------------------------------------

# Sum wil give total values of null values

pd.isnull(df).sum()

df.shape

df.columns

----------------------------------------------------------------------------------------------------------------------------------------------------
# Change Data Type
df[ 'ship-postal-code' ]=df[ 'ship-postal-code' ].astype('float')

df['ship-postal-code'].dtype

df['Date']=pd.to_datetime(df[ 'Date' ])

df.info()

df.columns

----------------------------------------------------------------------------------------------------------------------------------------------------
# Rename Columns
df.rename(columns={'Qty':'Quantity'})

df.describe(include='object')

----------------------------------------------------------------------------------------------------------------------------------------------------
# Use describe() for specific columns
df[['Qty','Amount']].describe()

----------------------------------------------------------------------------------------------------------------------------------------------------

# Exploratory Data Analysis
df.columns

*** Size :
ax = sns.countplot(x='Size',data=df)

*** Group By :

# The GroupBy() function in pandas is used to group data based on 1 or more columns in a Dataframe.


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


S_Qty=df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

sns.barplot(x='Size',y='Qty',data=S_Qty)


# From above Graph you can see that most of the Qty buys M-size in the sales.

*** Courier Status :

sns.countplot(data=df, x='Courier Status', hue= 'Status')

plt.figure(figsize=(10,5))
ax = sns.countplot(data=df, x='Courier Status', hue='Status')
plt.show()


# From Above Graph the majorityof the orders are shipped through the courier.

---------------------------------------------------------------------------------------------------------------------------------------------------
# Histogram

df['Size'].hist()

df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize = (10,5))
plt.hist(column_data, bins=20, edgecolor='Yellow')
plt.xticks(rotation=90)
plt.show()


# From above Graph you can see that most of the buyers are T-Shirt.
-----------------------------------------------------------------------------------------------------------------------------------------------

# Checking B2B Data by using pie chart

B2B_Check = df['B2B'].value_counts()

# Plot the pie chart

plt.pie(B2B_Check, labels=B2B_Check.index, autopct = '%1.1f%%')

# plt.axis('Equal')

plt.show()


# From above chart we can see that maximum i.e. 99.3% of buyers are retailers and 0.7% are B2B buyers.

------------------------------------------------------------------------------------------------------------------------------------------------------------

# Category and Size the products. 

# Prepare data for Scatter Plot :
x_data = df['Category']
y_data = df['Size']

# Plot the Scatter Plot
plt.scatter(x_data,y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.xticks(rotation=90)
plt.show()

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Which city or state buy the most of the products.

plt.figure(figsize=(12,6))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Top 10_states :
top_10_state = df['ship-state'].value_counts().head(10)

# Plot count of cities by state :

plt.figure(figsize=(12,6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=45)
plt.show()


# From above Graph you can see that most of the buyers are Maharastra State.

# -- Conclusion :

# The Data Analysis reveals that the business has a significant customers base in Maharastra State, mainly serves retailers, orders through Amazon, experiences high demand for T-shirt, and sees M-Size as the preferred choice among buyers.
