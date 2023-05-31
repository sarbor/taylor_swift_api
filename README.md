# Taylor Swift API
[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v1/monitor/q932.svg)](https://taylorswiftapi.betteruptime.com/)

The Taylor Swift API allows you to access information about Taylor Swift's albums, songs, and lyrics. You can retrieve data such as album details, song info and lyrics for a specific song.

You can even request N verses of lyrics from the api to use as Lorem Ipsum.

This API is hosted on Cloudflare Workers and the data is stored inside PlanetScale

[User Friendly Documentation for this API](https://bump.sh/sarbor/doc/taylor-swift-api)

Projects using this API
+ [Taylor Ipsum Generator](https://taylor-ipsum-website.pages.dev/)

## Base URL

The API is hosted at: `https://taylor-swift-api.sarbo.workers.dev`

## Endpoints

### Get all albums

Returns all Taylor Swift Albums.

- **Endpoint**: `/albums`
- **Method**: GET
- **Example Request**: Gets lyrics for song with song_id 10
    ```bash
    curl \
    -X GET "https://taylor-swift-api.sarbo.workers.dev/albums"
    ```
- **Response**: Returns an array of album objects.

  ```json
  [
    {
      "album_id": 1,
      "title": "1989",
      "release_date": "2014-10-27"
    },
    {
      "album_id": 2,
      "title": "Taylor Swift",
      "release_date": "2006-10-24"
    },
    ...
  ]
  ```


### Get songs within an album

Retrieve all songs within a specific album.

- **Endpoint**: `/albums/{albumID}`
- **Method**: GET
- **Parameters**:
  - `albumID` (integer, path): The ID of the album.

- **Example Request**: Returns all somgs within album with album_id 10
    ```bash
    curl \
    -X GET "https://taylor-swift-api.sarbo.workers.dev/albums/10"
    ```
- **Response**: Returns an array of song objects.

  ```json
  [
    {
        "song_id": 147,
        "title": "Snow on the Beach",
        "album_id": 10
    },
    {
        "song_id": 148,
        "title": "Maroon",
        "album_id": 10
    },
    {
        "song_id": 149,
        "title": "Bejeweled",
        "album_id": 10
    },
    {
        "song_id": 150,
        "title": "Labyrinth",
        "album_id": 10
    },
    {
        "song_id": 151,
        "title": "Mastermind",
        "album_id": 10
    },
    {
        "song_id": 152,
        "title": "Lavender Haze",
        "album_id": 10
    },
    {
        "song_id": 153,
        "title": "Sweet Nothing",
        "album_id": 10
    },
    {
        "song_id": 154,
        "title": "Vigilante Shit",
        "album_id": 10
    },
    {
        "song_id": 155,
        "title": "Midnight Rain",
        "album_id": 10
    },
    {
        "song_id": 156,
        "title": "Karma",
        "album_id": 10
    },
    {
        "song_id": 157,
        "title": "Anti-Hero",
        "album_id": 10
    },
    {
        "song_id": 158,
        "title": "Question…?",
        "album_id": 10
    },
    {
        "song_id": 159,
        "title": "You're on Your Own, Kid",
        "album_id": 10
    },
    {
        "song_id": 160,
        "title": "The Great War",
        "album_id": 10
    },
    {
        "song_id": 161,
        "title": "High Infidelity",
        "album_id": 10
    },
    {
        "song_id": 162,
        "title": "Would've, Could've, Should've",
        "album_id": 10
    },
    {
        "song_id": 163,
        "title": "Bigger Than the Whole Sky",
        "album_id": 10
    },
    {
        "song_id": 164,
        "title": "Paris",
        "album_id": 10
    },
    {
        "song_id": 165,
        "title": "Glitch",
        "album_id": 10
    },
    {
        "song_id": 166,
        "title": "Dear Reader",
        "album_id": 10
    },
    {
        "song_id": 176,
        "title": "Hits Different",
        "album_id": 10
    },
    {
        "song_id": 177,
        "title": "You're Losing Me",
        "album_id": 10
    }
  ]
   ```
 

### Get all songs

Retrieve all songs within ALL albums.

- **Endpoint**: `/songs`
- **Method**: GET
- **Example Request**: Gets all songs
    ```bash
    curl \
    -X GET "https://taylor-swift-api.sarbo.workers.dev/songs"
    ```
- **Response**: Returns an array of song objects.

  ```json
  [
    {
      "song_id": 1,
      "title": "Blank Space",
      "album_id": 1
    },
    {
      "song_id": 2,
      "title": "Style",
      "album_id": 1
    },
    ...
  ]
  ```


### Get song information for a specific song

Retrieve song information for a specific song.

- **Endpoint**: `/songs/{songID}`
- **Method**: GET
- **Parameters**:
  - `songID` (path parameter): ID of the song (integer)
- **Example Request**: Gets song info for song with song_id 10
    ```bash
    curl \
    -X GET "https://taylor-swift-api.sarbo.workers.dev/songs/10"
    ```
- **Response**: Returns a song object.

  ```json
  {
    "song_id": 10,
    "song_title": "Wonderland",
    "album_id": 1
  }
  ```


### Get lyrics for a given song

Retrieve the lyrics for a given song.

- **Endpoint**: `/lyrics/{songID}`
- **Method**: GET
- **Parameters**:
  - `songID` (path parameter): ID of the song (integer)
- **Example Request**: Gets lyrics for song with song_id 10
    ```bash
    curl \
    -X GET "https://taylor-swift-api.sarbo.workers.dev/lyrics/10"
    ```
- **Response**: Returns a song's lyrics.

  ```json
  {
    "song_id": 10,
    "song_title": "Wonderland",
    "lyrics": "Flashing lights and we\nTook a wrong turn and we\nFell down a rabbit hole\n\nYou held on tight to me\n'Cause nothing's as it seems\nAnd spinning out of control\n\nDidn't they tell us don't rush into things?\nDidn't you flash your green eyes at me?\nHaven't you heard what becomes of curious minds?\n\nOh\n\nDidn't it all seem new and exciting?\nI felt your arms twisting around me\nI should have slept with one eye open at night\n\nWe found wonderland\nYou and I got lost in it\nAnd we pretended it could last forever\nEh\nWe found wonderland\nYou and I got lost in it\nAnd life was never worse but never better\nEh eh\n\nEh eh eh eh eh\nIn wonderland\nEh eh eh eh eh\nIn wonderland\nEh eh eh eh eh\nIn wonderland\nEh eh eh eh eh\nIn wonderland\n\nSo we went on our way\nToo in love to think straight\nAll alone or so it seemed\n\nBut there were strangers watching\nAnd whispers turned to talking\nAnd talking turned to screams\n\nOh\n\nDidn't they tell us don't rush into things?\nDidn't you flash your green eyes at me?\nDidn't you calm my fears with a Cheshire cat smile?\n\nOh\n\nDidn't it all seem new and exciting?\nI felt your arms twisting around me\nIt's all fun and games 'til somebody loses their mind\n\nBut darling, we found wonderland\nYou and I got lost in it\nAnd we pretended it could last forever\nEh\nWe found wonderland\nYou and I got lost in it\nAnd life was never worse but never better\nEh eh\n\nEh eh eh eh eh\nIn wonderland\nEh eh eh eh eh\nIn wonderland\nEh eh eh eh eh\nIn wonderland\nEh eh eh eh eh\nIn wonderland\n\nI reached for you but you were gone\nI knew I had to go back home\nYou searched the world for something else to make you feel like what we had\nAnd in the end in wonderland we both went mad\n\nOh\n\nWe found wonderland\nYou and I got lost in it\nAnd we pretended it could last forever (last forever)\nEh eh\nWe found wonderland\nYou and I got lost in it (got lost in it)\nAnd life was never worse but never better (never better)\nEh eh\n\nWe found wonderland\nYou and I got lost in it (wonderland)\nAnd we pretended it could last forever (in wonderland)\n\nWe found wonderland\nYou and I got lost in it (wonderland)\nAnd life was never worse but never better\nIn wonderland"
  }
  ```

### Get N Paragraphs of Lyrics

Retrieve N paragraphs of lyrics from songs. The songs can be either random or in the default order.

The endpoint will keep retrieving lyrics from a song until there are no lyrics left. If there are not enough paragraphs in the song to fulfill `numberOfParagraphs` requested, it will pick another song and start from the beginning

- **Endpoint**: `/lyrics`
- **Method**: GET
- **Parameters**:
  - `shouldRandomizeLyrics` (query parameter): Flag indicating whether to randomize the order of lyrics (boolean)
  - `numberOfParagraphs` REQUIRED (query parameter): Number of paragraphs of lyrics to retrieve (integer)
- **Example Request**: Returns 2 paragraphs of lyrics from songs from random songs.
    ```bash
    curl \
    -X GET "https://taylor-swift-api.sarbo.workers.dev/lyrics?shouldRandomizeLyrics=true&numberOfParagraphs=2"
    ```

- **Response**: Returns 2 paragraphs of lyrics from randomized songs songs.

  ```json
    {
        "lyrics": [
            "He says he doesn't believe anything much he hears these days\nHe says, \"Why fall in love, just so you can watch it go away?\"\nHe spends most of his nights wishing it was how it used to be\nHe spends most of his flights getting pulled down by gravity\nI call, just checking up on him\nHe's up, 3 A.M., pacing\nHe says, \"It's not just a phase I'm in\"\nMy voice comes out begging",
            "All this time I didn't know\nYou were breaking down\nI'd fall to pieces on the floor\nIf you weren't around\nToo young to know it gets better\nI'll be summer sun for you forever\nForever winter if you go"
        ],
        "numParagraphs": 2
    }
 ```
