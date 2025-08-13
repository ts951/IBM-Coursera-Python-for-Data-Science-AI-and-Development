"""
This sript experiments with working with different file formats in python
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import json
import xml.etree.ElementTree as ET
from PIL import Image

"""
Next section is on CSV
"""
print("CSV!\n")
# Download csv file from url as a dataframe
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
df = pd.read_csv(url)

# Add column names
df.columns = ["First Name", "Last Name", "Location", "City", "State", "Area Code"]

print("DataFrame retrieved from CSV file", df)

"""
Real quick: the transform function in pandas
"""

print("\nTransform function in Pandas!\n")
# Apply a couple transform functions to the following dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df_plus_10 = df.transform(func = lambda x : x + 10)
df_sqrt = df.transform(func = ["sqrt"])
print("Original DataFrame\n", df)
print("Add 10 to each element using transform function\n", df_plus_10)
print("Square root of each element\n", df_sqrt)

"""
Next section is on JSON
"""

print("\nJSON!\n")

# Serialisation!

# Write data in following dataframe to a JSON file using dump
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open("person_using_dump.json", "w") as f:
    json.dump(person, f)
    print("person_using_dump.json created!")

# Now convert the dictionary to a JSON object using dumps then write to the file
# result should be the same but with indentation
json_object = json.dumps(person, indent = 4)

with open("person_using_dumps.json", "w") as f:
    f.write(json_object)
    print("person_using_dumps.json created!")

# Deserialisation

# Now lets store data from a JSON file as an object in python
with open("person_using_dumps.json", "r") as f:
    json_object = json.load(f)
    print("JSON object recreated using load method on the previously created files:\n", json_object)
    print("This is of type: ", type(json_object))

"""
Following section is on XLSX
"""

print("\nXLSX!\n")

# Download xlsx file from url
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
df = pd.read_excel(url)
print("Data from XLSX file:\n", df)

"""
Following section on XML
"""

print("\nXML!\n")

# Create a new XML file
employee = ET.Element("employee")

details = ET.SubElement(employee, "details")

first = ET.SubElement(details, "firstname")
second = ET.SubElement(details, "lastname")
third = ET.SubElement(details, "age")

first.text = "Shiv"
second.text = "Mishra"
third.text = "23"

et_data = ET.ElementTree(employee)

with open("sample.xml", "wb") as f:
    et_data.write(f)
    print("New xml file created!")

# Get a dataframe from the xml file
df = pd.read_xml("sample.xml") 
print("DataFrame created from the previously created XML file\n", df)

"""
Binary files section!
"""

print("\nBinary Files! For example an image\n")

# Show the laddy!
img = Image.open("./P4_Red_Pikmin.webp", "r")
img.show()