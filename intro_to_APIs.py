"""
This script experiments with Pandas as an API and REST APIs
as well as muckin about with the data a bit
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams

"""
Following section involves pandas, and how it uses APIs
"""

# Create a dictionary, this is just data
dict = {'a':[11,21,31],'b':[12,22,32]}

# Create a Pandas object with the dataframe constructor (an instance),
# data in dictionary is passed along to pandas API and we use the dataframe 
# to communicate with the API. Nice!
df = pd.DataFrame(dict)
# Print the data type of the dataframe
print("DataFrame's type:\n", type(df))

# Calling method head() for example communicates with the API, returning 
# the first few rows of the dataframe
print("DataFrame:\n", df.head())

# When you call mean() method, API calculates the mean and returns it!
print("Mean of data in DataFrame:\n", df.mean())

"""
Next section is on REST APIs, specifically using the NBA API to get
NBA data
"""