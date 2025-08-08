"""
This script experiments with Pandas as an API and REST APIs
as well as muckin about with the data a bit
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import requests

# Function to create a single dictionary from a list of dictionaries
def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# Function for downloading files from a url
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

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
print("Mean of data in DataFrame:\n", df.mean(), "\n")

"""
Next section is on REST APIs, specifically using the NBA API to get
NBA data
"""

# Use get_teams method to get a list of dictionaries containing NBA team data
nba_teams = teams.get_teams()

# Convert this into a table by converting it into a single dictionary then a dataframe
dict_nba_team = one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
# Print first 5 collumns
print("First 5 collumns of teams dataframe:\n", df_teams.head(), "\n")

# Access the "Warriors" row using the nickname
df_warriors = df_teams[df_teams["nickname"] == "Warriors"]
print("Warriors row:\n", df_warriors, "\n")

# Access the id from the Warriors row
id_warriors = df_warriors.loc[df_warriors.index.values[0], "id"]
print("Warriors id:\n", id_warriors, "\n")

# Find Warriors game data!
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
games_warriors = gamefinder.get_data_frames()[0]

print("First five warriors games in dataframe\n", games_warriors.head(), "\n")

# Download dataframe from the API call for Golden State Warriors
filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
download(filename, "Golden_State.pkl")
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)

# Note, the dataframe it gets is different, fair play
print("Games head again, just accessed a different way\n", games.head(), "\n")

# Create separate dataframes for home vs away games
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

# Calculate the mean for the collumn PLUS_MINUS for home and away games
# We can compare woo!
print("Mean PLUS_MINUS value for home games: ", games_home['PLUS_MINUS'].mean(), "\n")
print("Mean PLUS_MINUS value for away games: ", games_away['PLUS_MINUS'].mean(), "\n")

# Plot out!
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

# Ok test time
# Calculate mean for column PTS in the home and away dataframes
print("Mean PTS value for home games: ", games_home['PTS'].mean(), "\n")
print("Mean PTS value for away games: ", games_away['PTS'].mean(), "\n")