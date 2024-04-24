from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import json
import logging

# Define Pydantic models for the data structures
class Album(BaseModel):
    album_id: int
    title: str
    release_date: str

class Song(BaseModel):
    song_id: int
    title: str
    album_id: int

class Lyrics(BaseModel):
    song_id: int
    song_title: str
    lyrics: str

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the route handlers
@app.get("/albums", response_model=List[Album])
async def get_albums():
    # Placeholder for reading albums from a JSON file
    with open("albums.json", "r") as f:
        albums = json.load(f)
    return albums

@app.get("/albums/{albumID}", response_model=List[Song])
async def get_album_songs(albumID: int):
    try:
        # Placeholder for reading songs from a JSON file
        with open("songs.json", "r") as f:
            songs = json.load(f)
        album_songs = [song for song in songs if song['album_id'] == albumID]
        if not album_songs:
            raise HTTPException(status_code=404, detail="Album not found")
        return album_songs
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error: Error reading songs data")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/songs", response_model=List[Song])
async def get_songs():
    # Placeholder for reading songs from a JSON file
    with open("songs.json", "r") as f:
        songs = json.load(f)
    return songs

@app.get("/songs/{songID}", response_model=Song)
async def get_song(songID: int):
    # Placeholder for reading songs from a JSON file
    with open("songs.json", "r") as f:
        songs = json.load(f)
    song = next((song for song in songs if song['song_id'] == songID), None)
    if song:
        return song
    else:
        raise HTTPException(status_code=404, detail="Song not found")

@app.get("/lyrics/{songID}", response_model=Lyrics)
async def get_lyrics(songID: int):
    # Placeholder for reading lyrics from a JSON file
    with open("lyrics.json", "r") as f:
        lyrics_data = json.load(f)
    lyrics = next((item for item in lyrics_data if item['song_id'] == songID), None)
    if lyrics:
        return lyrics
    else:
        raise HTTPException(status_code=404, detail="Lyrics not found")

# Additional route for /lyrics with query parameters will be added later
