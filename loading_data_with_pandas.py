"""
This script explores accessing and viewing data using Pandas (the library not the animal :O)
"""

# Import necessary library
import pandas as pd

# Get product sales data in CSV format from URL and store as a dataframe
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv")

# Can also do it from an excel file with:
# df = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx')

# Double square brackets gives us a collumn as another dataframe
quantities = df[["Quantity"]]
print("Quantity collumn as a pandas dataframe:\n", quantities, "\n")

# Single square brackets gives us a collumn as a pandas series
quantities_series = df["Quantity"]
print("Quantity collumn as a pandas series:\n", quantities_series, "\n")

"""
Quiz section answers!
"""

# Store price collumn as a dataframe
prices = df[["Price"]]
print("Price collumn as a dataframe:\n", prices, "\n")

# Store product and category collumns in a single dataframe
products_and_categories = df[["Product", "Category"]]
print("Dataframe containing product and category collumns:\n", products_and_categories, "\n")

# Store the element in the 2nd row and the 3rd collumn
second_row_third_collumn = df.iloc[1, 2]
print("Element in the 2nd row and the 3rd collumn:\n", second_row_third_collumn, "\n")

# Convert dataframe's indexes to the characters in the following list
new_index = ["a", "b", "c", "d", "e"]

df.index = new_index
print("Newly indexed dataframe\n:", df, "\n")

# Store element corresponding to row "a" collumn "CustomerCity"
row_a_city = df.loc["a", "CustomerCity"]
print("Element in row \"a\", collumn \"CustomerCity\":\n", row_a_city, "\n")

# Store rows "a" through "d" for collumn "CustomerCity"
rows_a_to_d_cities = df.loc["a": "d", "CustomerCity"]
print("Customer cities for rows a through d:\n", rows_a_to_d_cities, "\n")