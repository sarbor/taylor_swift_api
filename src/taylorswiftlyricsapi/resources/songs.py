# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.song_list_response import SongListResponse
from ..types.song_retrieve_response import SongRetrieveResponse

__all__ = ["SongsResource", "AsyncSongsResource"]


class SongsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SongsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sarbor/taylor_swift_api#accessing-raw-response-data-eg-headers
        """
        return SongsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SongsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sarbor/taylor_swift_api#with_streaming_response
        """
        return SongsResourceWithStreamingResponse(self)

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
    ) -> SongRetrieveResponse:
        """
        Get song information for a specific song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/songs/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SongRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SongListResponse:
        """Get all songs"""
        return self._get(
            "/songs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SongListResponse,
        )


class AsyncSongsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSongsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sarbor/taylor_swift_api#accessing-raw-response-data-eg-headers
        """
        return AsyncSongsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSongsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sarbor/taylor_swift_api#with_streaming_response
        """
        return AsyncSongsResourceWithStreamingResponse(self)

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
    ) -> SongRetrieveResponse:
        """
        Get song information for a specific song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/songs/{song_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SongRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SongListResponse:
        """Get all songs"""
        return await self._get(
            "/songs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SongListResponse,
        )


class SongsResourceWithRawResponse:
    def __init__(self, songs: SongsResource) -> None:
        self._songs = songs

        self.retrieve = to_raw_response_wrapper(
            songs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            songs.list,
        )


class AsyncSongsResourceWithRawResponse:
    def __init__(self, songs: AsyncSongsResource) -> None:
        self._songs = songs

        self.retrieve = async_to_raw_response_wrapper(
            songs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            songs.list,
        )


class SongsResourceWithStreamingResponse:
    def __init__(self, songs: SongsResource) -> None:
        self._songs = songs

        self.retrieve = to_streamed_response_wrapper(
            songs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            songs.list,
        )


class AsyncSongsResourceWithStreamingResponse:
    def __init__(self, songs: AsyncSongsResource) -> None:
        self._songs = songs

        self.retrieve = async_to_streamed_response_wrapper(
            songs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            songs.list,
        )
