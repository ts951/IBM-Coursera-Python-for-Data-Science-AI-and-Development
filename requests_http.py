"""
This script experiments with HTTP and requests in python
(not much though lmao)
"""

# Import required libraries
import requests
import os
from PIL import Image

# Download the text file in the following link
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"

# Specify file path and name for text file to be stored in and as
path = os.path.join(os.getcwd(), "Example1.txt")

# Make get request
r = requests.get(url)

# Write the content of the response body to the local txt file
with open(path, "wb") as f:
    f.write(r.content)