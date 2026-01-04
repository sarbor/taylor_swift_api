# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AlbumListResponse", "AlbumListResponseItem"]


class AlbumListResponseItem(BaseModel):
    album_id: Optional[int] = None

    release_date: Optional[date] = None

    title: Optional[str] = None


AlbumListResponse: TypeAlias = List[AlbumListResponseItem]
