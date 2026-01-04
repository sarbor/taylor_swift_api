# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import lyric_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.lyric_list_response import LyricListResponse
from ..types.lyric_retrieve_response import LyricRetrieveResponse

__all__ = ["LyricsResource", "AsyncLyricsResource"]


class LyricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LyricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taylorswiftlyricsapi-python#accessing-raw-response-data-eg-headers
        """
        return LyricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LyricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taylorswiftlyricsapi-python#with_streaming_response
        """
        return LyricsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        song_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LyricRetrieveResponse:
        """
        Get lyrics for a given song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/lyrics/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LyricRetrieveResponse,
        )

    def list(
        self,
        *,
        number_of_paragraphs: int | Omit = omit,
        should_randomize_lyrics: Literal | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LyricListResponse:
        """
        Get N paragraphs of lyrics from songs

        Args:
          number_of_paragraphs: Number of paragraphs of lyrics to retrieve

          should_randomize_lyrics: Indicates whether to randomize the lyrics or use default order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/lyrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "number_of_paragraphs": number_of_paragraphs,
                        "should_randomize_lyrics": should_randomize_lyrics,
                    },
                    lyric_list_params.LyricListParams,
                ),
            ),
            cast_to=LyricListResponse,
        )


class AsyncLyricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLyricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taylorswiftlyricsapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLyricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLyricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taylorswiftlyricsapi-python#with_streaming_response
        """
        return AsyncLyricsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        song_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LyricRetrieveResponse:
        """
        Get lyrics for a given song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/lyrics/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LyricRetrieveResponse,
        )

    async def list(
        self,
        *,
        number_of_paragraphs: int | Omit = omit,
        should_randomize_lyrics: Literal | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LyricListResponse:
        """
        Get N paragraphs of lyrics from songs

        Args:
          number_of_paragraphs: Number of paragraphs of lyrics to retrieve

          should_randomize_lyrics: Indicates whether to randomize the lyrics or use default order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/lyrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "number_of_paragraphs": number_of_paragraphs,
                        "should_randomize_lyrics": should_randomize_lyrics,
                    },
                    lyric_list_params.LyricListParams,
                ),
            ),
            cast_to=LyricListResponse,
        )


class LyricsResourceWithRawResponse:
    def __init__(self, lyrics: LyricsResource) -> None:
        self._lyrics = lyrics

        self.retrieve = to_raw_response_wrapper(
            lyrics.retrieve,
        )
        self.list = to_raw_response_wrapper(
            lyrics.list,
        )


class AsyncLyricsResourceWithRawResponse:
    def __init__(self, lyrics: AsyncLyricsResource) -> None:
        self._lyrics = lyrics

        self.retrieve = async_to_raw_response_wrapper(
            lyrics.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            lyrics.list,
        )


class LyricsResourceWithStreamingResponse:
    def __init__(self, lyrics: LyricsResource) -> None:
        self._lyrics = lyrics

        self.retrieve = to_streamed_response_wrapper(
            lyrics.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            lyrics.list,
        )


class AsyncLyricsResourceWithStreamingResponse:
    def __init__(self, lyrics: AsyncLyricsResource) -> None:
        self._lyrics = lyrics

        self.retrieve = async_to_streamed_response_wrapper(
            lyrics.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            lyrics.list,
        )
