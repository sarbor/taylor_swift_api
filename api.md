# Albums

Types:

```python
from taylorswiftlyricsapi.types import AlbumListResponse, AlbumRetrieveSongsResponse
```

Methods:

- <code title="get /albums">client.albums.<a href="./src/taylorswiftlyricsapi/resources/albums.py">list</a>() -> <a href="./src/taylorswiftlyricsapi/types/album_list_response.py">AlbumListResponse</a></code>
- <code title="get /albums/{albumID}">client.albums.<a href="./src/taylorswiftlyricsapi/resources/albums.py">retrieve_songs</a>(album_id) -> <a href="./src/taylorswiftlyricsapi/types/album_retrieve_songs_response.py">AlbumRetrieveSongsResponse</a></code>

# Songs

Types:

```python
from taylorswiftlyricsapi.types import SongRetrieveResponse, SongListResponse
```

Methods:

- <code title="get /songs/{songID}">client.songs.<a href="./src/taylorswiftlyricsapi/resources/songs.py">retrieve</a>(song_id) -> <a href="./src/taylorswiftlyricsapi/types/song_retrieve_response.py">SongRetrieveResponse</a></code>
- <code title="get /songs">client.songs.<a href="./src/taylorswiftlyricsapi/resources/songs.py">list</a>() -> <a href="./src/taylorswiftlyricsapi/types/song_list_response.py">SongListResponse</a></code>

# Lyrics

Types:

```python
from taylorswiftlyricsapi.types import LyricRetrieveResponse, LyricListResponse
```

Methods:

- <code title="get /lyrics/{songID}">client.lyrics.<a href="./src/taylorswiftlyricsapi/resources/lyrics.py">retrieve</a>(song_id) -> <a href="./src/taylorswiftlyricsapi/types/lyric_retrieve_response.py">LyricRetrieveResponse</a></code>
- <code title="get /lyrics">client.lyrics.<a href="./src/taylorswiftlyricsapi/resources/lyrics.py">list</a>(\*\*<a href="src/taylorswiftlyricsapi/types/lyric_list_params.py">params</a>) -> <a href="./src/taylorswiftlyricsapi/types/lyric_list_response.py">LyricListResponse</a></code>
