#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'Germany', 'Germany'],
    'Year': [2020, 2021, 2020, 2021, 2020, 2021],
    'Population': [331000000, 331000000, 1402000000, 1402000000, 83000000, 83100000],
    'GDP': [21000000, 21500000, 14700000, 15500000, 4000000, 4200000],
    'Life_Expectancy': [78.5, 78.7, 76.9, 77.1, 81.5, 81.5]
}

df = pd.DataFrame(data)
df.set_index(['Country', 'Year'], inplace=True)
print("Original DataFrame:\n", df, "\n")

print("Mean Population:", df['Population'].mean())
print("Total GDP:", df['GDP'].sum())
print("Max Life Expectancy:", df['Life_Expectancy'].max())
print("Standard Deviation of GDP (NumPy):", np.std(df['GDP']), "\n")
df['GDP'] = df['GDP'] * 1.10
print("GDP increased by 10%:\n", df, "\n")
df_swapped = df.swaplevel('Country', 'Year')
df_swapped = df_swapped.sort_index(level='Year')
print("After swaplevel (sorted by Year):\n", df_swapped, "\n")
df_unstacked = df.unstack(level='Year')
print("Unstacked Data (Year as columns):\n", df_unstacked, "\n")
china_data = df.loc['China']
print("China Population Trend:\n", china_data['Population'], "\n")
gdp_2021 = df.xs(2021, level='Year')['GDP']
print("GDP of all countries in 2021:\n", gdp_2021)


# In[ ]:




