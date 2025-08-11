"""
More examples of how to use simple APIs in this script!
"""

# import required libraries
from randomuser import RandomUser
import pandas as pd
import requests
import json

"""
Next section is on RandomUser API
"""

# Function to generate a dataframe of information about 10 random users
def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name" : user.get_full_name(), "Gender" : user.get_gender(), "City" : user.get_city(), "State" : user.get_state(), "Email" : user.get_email(), "DOB" : user.get_dob(), "Picture" : user.get_picture()})

    return pd.DataFrame(users)  


# Create random user object
r = RandomUser()

# Generate a list of 10 random users using this object
user_list = r.generate_users(10)
print("List of random users!\n", user_list)

# Can get the name of the RandomUser object
print("\nname from r: ", r.get_full_name())

# Lets print the names and emails generated in the 10 user list
print("\nNames and emails of all the randomly generated dudes:")
for user in user_list:
    print("\t", user.get_full_name(), " ", user.get_email())

# Ok lets get random pictures for the users
print("\nURLs to all the pictures of all the randomly generated dudes")
for user in user_list:
    print("\t", user.get_picture())

# Now let's try out our function
users_df = get_users()
print(users_df)


"""
Next section is on the FruityVice API
"""

# Obtain fruityvice API data
fruity_vice_data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
# Retrieve results
fruity_vice_results = json.loads(fruity_vice_data.text)
# Normalise JSON and convert into a dataframe
fruity_vice_df = pd.json_normalize(fruity_vice_results)

banana = fruity_vice_df.loc[fruity_vice_df["name"] == "Banana"]
print("\nThe number of calories in a banana is: ", banana.iloc[0]["nutritions.calories"])

"""
Let's try a new API! Official Joke API
"""
# Get the jopke data from the api
joke_data = requests.get("https://official-joke-api.appspot.com/jokes/ten")

# Retrieve results as a datafram
joke_df = pd.json_normalize(json.loads(joke_data.text))

# Drop the lame columns type and id
joke_df.drop(columns = ["type", "id"], inplace = True)

print(joke_df) # Omg these are great