# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LyricRetrieveResponse"]


class LyricRetrieveResponse(BaseModel):
    lyrics: Optional[str] = None

    song_id: Optional[int] = None

    song_title: Optional[str] = None
