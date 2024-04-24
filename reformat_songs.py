import json

# Read the original file
with open('songs.json', 'r') as file:
    songs_data = json.load(file)

# Assuming albums.json is correctly formatted and contains album_id
with open('albums.json', 'r') as file:
    albums_data = json.load(file)

# Create a dictionary to map album titles to album_ids
album_title_to_id = {album['title']: album['album_id'] for album in albums_data}

# Initialize song_id counter
song_id = 1

# Reformat songs data with correct keys and add song_id and album_id
reformatted_songs = []
for song in songs_data:
    album_title = song['Album']
    if album_title in album_title_to_id:
        reformatted_song = {
            'song_id': song_id,
            'title': song['Song Name'],
            'album_id': album_title_to_id[album_title]
        }
        reformatted_songs.append(reformatted_song)
        song_id += 1

# Write the reformatted list of song objects as a JSON array to the file
with open('songs.json', 'w') as file:
    json.dump(reformatted_songs, file, indent=4)
