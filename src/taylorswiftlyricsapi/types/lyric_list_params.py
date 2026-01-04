# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LyricListParams"]


class LyricListParams(TypedDict, total=False):
    number_of_paragraphs: Annotated[int, PropertyInfo(alias="numberOfParagraphs")]
    """Number of paragraphs of lyrics to retrieve"""

    should_randomize_lyrics: Annotated[Literal, PropertyInfo(alias="shouldRandomizeLyrics")]
    """Indicates whether to randomize the lyrics or use default order"""
