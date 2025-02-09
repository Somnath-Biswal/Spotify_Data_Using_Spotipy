# Install spotipy
!pip install spotipy

# import spotipy and the credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials # these module has a function named SpotifyClientCredentials

# Your Spotify credentials: You can get this after setting up a Spotify Developer's account

cid = 'your client id' # spotify credentials has two parts client id and secret key for authorization
secret = 'client secret'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) # input credentials
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = [] # List to store the artist name
track_name = [] # List to store the track name
popularity = [] # List to store the popularity of the track
track_id = [] # List to store the track ID

# Spotify allows to set an offset upto 1000
for i in range(0,1000,50):
  # Nested loops to extract data for 4 years i.e 2018, 2019, 2020, 2021
  for year in range(2018, 2022):
    # Search the data for the particular year
    track_results = sp.search(q='year:{}'.format(year), type='track', limit=50,offset=i)
    # Iterate over the results and store the required fields
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

# Using pandas to creat a dataframe
import pandas as pd
track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
track_dataframe.head()

# Store the data in a csv file
track_dataframe.to_csv("./spotify_data.csv", index=False)
