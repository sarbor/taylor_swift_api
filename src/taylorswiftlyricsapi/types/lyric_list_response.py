# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LyricListResponse"]


class LyricListResponse(BaseModel):
    lyrics: Optional[List[str]] = None

    num_paragraphs: Optional[int] = None
