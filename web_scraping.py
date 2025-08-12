"""
This script experiments with web scraping using the Beautiful Soup library
From Coursera Labs
"""

# Import required libraries
from bs4 import BeautifulSoup
import requests

# Little example without using requests to retrieve the html from a website
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
print("Example HTML stored in a BeautifulSoup object:\n\n", soup.prettify(), "\n") # Print it in a nested structure (pretty!)

# Extract the title tag of the page from the BeautifulSoup object as an object
title_object = soup.title
print("Tag object from soup: ", title_object)
print("Tag object type: ", type(title_object))

# Extract the first h3 tag from the soup object
h3_object = soup.h3
print("First h3 object in soup: ", h3_object)

# Get this objects child component
h3_child_b = h3_object.b
print("First h3 object's child: ", h3_child_b)

# Get the child's parent component (should be the same as tag_object)
tag_parent = h3_child_b.parent
print("Parent of the child: ", tag_parent) 

# Get the first 2 of the h3 tag's siblings
sibling_1 = h3_object.next_sibling
sibling_2 = sibling_1.next_sibling
print("The first h3 tag's siblings are:\n", sibling_1, "\nand:\n", sibling_2)

# Access id attribute of h3's first child b
print("First h3 tag's first child's id attribute: ", h3_child_b["id"])

# Access attributes dictionary of h3's first child b
print("First h3 tag's first child's attributes dictionary: ", h3_child_b.attrs)

# Access the text within the tag as a navigable string
h3_child_b_string = h3_child_b.string
print("Tag contains the following text: ", h3_child_b_string, ", which is stored as type: ", type(h3_child_b_string))

"""
Next section on filters!
"""

# Store table html as BeautifulSoup object
table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

# Use method find_all() to filter through the table and get all the table's rows
table_rows = table_bs.find_all("tr")

# iterate through this list and iterate through cells in each row and print em!
for i, row in enumerate(table_rows):
    print("Row ", i, ", ")
    cells = row.find_all("td")
    for j, cell in enumerate(cells):
        print("column, ", j, ", cell is: ", cell)

# find all <a> tags without an href value in the table
table_addresses_no_href = table_bs.find_all("a", href = False)
print("<a> tags without an href value:\n", table_addresses_no_href)

"""
Ok following section is regarding these two tables
"""

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

two_tables_bs = BeautifulSoup(two_tables, "html.parser")

# Find and print just the pizza table
print("Pizza table: \n", two_tables_bs.find("table", class_ = "pizza"))

"""
Following section is on downloading and then scraping the contents of a web page
"""

# Get html from url and create BeautifulSoup object
url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

# scrape all links!
print("Links in http://www.ibm.com\n\n")
for link in soup.find_all("a", href = True):
    print(link["href"])

# Ok now scrape data from the firsttable on the following site
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
table = soup.find("table")

# For each row in the table, get the colour from the 3rd collumn and the colour code from the 4th collumn and print to terminal
for row in table.find_all("tr"):
    cells = row.find_all("td")
    colour_name = cells[2].string
    colour_code = cells[3].string
    print(colour_name, "--->", colour_code)