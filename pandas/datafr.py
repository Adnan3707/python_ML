# %%
import numpy as np
import pandas as pd

arr = np.random.randint(0,100,(4,3))

# %%
arr
# %%
myindex = ['CA','NY','AZ','TX']

mycolumns = ['Jan','Feb','Mar']

# %%
df = pd.DataFrame(data=arr,index=myindex,columns=mycolumns)
# %%
df
# %%
df = pd.read_csv('C:/Interview Process/python_ML/pandas/hotel_booking_data.csv')

df.head()
# %%
# Columns
df = df.drop('arrival_date_week_number',axis=1)

# %%
df.columns
# %%
#  Working With rows
df = df.set_index('credit_card')
# %%
df.head()
# %%
df.iloc[0]
# %%
df.loc['************5498']
# %%
df.loc[['************5498','************5677']]
# %%
df.drop('************5677',axis=0)