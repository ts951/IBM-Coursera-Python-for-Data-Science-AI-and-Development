"""
This script just explores the functionality of DataFrames in the pandas library ^.__.^
"""

import pandas as pd


"""
Following section handles creating the dataframe and just checking how its all stored and whatnot
"""

# Define a dictionary 'students'
students_dict = {"Student": ["David", "Samuel", "Terry", "Evan"], 
            "Age": [27, 24, 22, 32], 
            "Country": ["UK", "Canada", "China", "USA"], 
            "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"], 
            "Marks": [85, 72, 89, 76]}

# Cast the dictionary to a DataFrame and print
students = pd.DataFrame(students_dict)
print("Students: \n", students, "\n")

# Retrieve and display students' marks
marks = students[["Marks"]]
print("Marks: \n", marks, "\n")

# Retrieve and display students' countries and courses
countries_courses = students[["Country", "Course"]]
print("Countries and Courses: \n", countries_courses, "\n")


"""
Following section experiments with loc and iloc functions
"""

# Display the value in the first row first collumn of the students dataframe
print("Element in the first row and first collumn of students: \n", students.iloc[0, 0], "\n")

# Display the value in the first row third collumn of the students dataframe
print("Element in the first row and third collumn of students: \n", students.iloc[0, 2], "\n")

# Display the value in the first row and the collumn named "Marks" in the students dataframe
print("Element in the first row and the \"Marks\" collumn of students: \n", students.loc[0, "Marks"], "\n")

# Set "Student" collumn as an index collumn and display updated dataframe as a list
students = students.set_index("Student")
print("Students: \n", students, "\n")

# Display the value in the David's row and the collumn named "Marks" in the students dataframe, should be the same as 0, "Marks" now
print("Element in the \"David\" and the \"Marks\" collumn of students: \n", students.loc["David", "Marks"], "\n")

# Dislay Terry's Course using loc with the updated dataframe
print("Terry's Course is: \n", students.loc["Terry", "Course"], "\n")

# Dislay Terry's Course using iloc with the updated dataframe
print("Terry's Course is: \n", students.iloc[2, 2], "\n")


"""
Following section experiments with slicing
"""

# Use loc() to retrieve Course and Marks where index column is Student having labels Samuel, Terry, and Evan (note that loc is inclusive whereas iloc is not includive of the upper one)
print("Course and Marks where index column is Student having labels Samuel, Terry, and Evan\n", students.loc["Samuel": "Evan", "Course": "Marks"], "\n") 
# ^^ Weird wording on the lab notes tbh, Should reword when I get the chance