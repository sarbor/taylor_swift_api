# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SongListResponse", "SongListResponseItem"]


class SongListResponseItem(BaseModel):
    album_id: Optional[int] = None

    song_id: Optional[int] = None

    title: Optional[str] = None


SongListResponse: TypeAlias = List[SongListResponseItem]
