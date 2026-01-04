# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AlbumRetrieveSongsResponse", "AlbumRetrieveSongsResponseItem"]


class AlbumRetrieveSongsResponseItem(BaseModel):
    album_id: Optional[int] = None

    song_id: Optional[int] = None

    title: Optional[str] = None


AlbumRetrieveSongsResponse: TypeAlias = List[AlbumRetrieveSongsResponseItem]
