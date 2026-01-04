# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SongRetrieveResponse"]


class SongRetrieveResponse(BaseModel):
    album_id: Optional[int] = None

    song_id: Optional[int] = None

    song_title: Optional[str] = None
