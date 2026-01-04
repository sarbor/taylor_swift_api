# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from taylorswiftlyricsapi import Taylorswiftlyricsapi, AsyncTaylorswiftlyricsapi
from taylorswiftlyricsapi.types import AlbumListResponse, AlbumRetrieveSongsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlbums:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Taylorswiftlyricsapi) -> None:
        album = client.albums.list()
        assert_matches_type(AlbumListResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Taylorswiftlyricsapi) -> None:
        response = client.albums.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album = response.parse()
        assert_matches_type(AlbumListResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Taylorswiftlyricsapi) -> None:
        with client.albums.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album = response.parse()
            assert_matches_type(AlbumListResponse, album, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_songs(self, client: Taylorswiftlyricsapi) -> None:
        album = client.albums.retrieve_songs(
            0,
        )
        assert_matches_type(AlbumRetrieveSongsResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_songs(self, client: Taylorswiftlyricsapi) -> None:
        response = client.albums.with_raw_response.retrieve_songs(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album = response.parse()
        assert_matches_type(AlbumRetrieveSongsResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_songs(self, client: Taylorswiftlyricsapi) -> None:
        with client.albums.with_streaming_response.retrieve_songs(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album = response.parse()
            assert_matches_type(AlbumRetrieveSongsResponse, album, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAlbums:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        album = await async_client.albums.list()
        assert_matches_type(AlbumListResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        response = await async_client.albums.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album = await response.parse()
        assert_matches_type(AlbumListResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        async with async_client.albums.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album = await response.parse()
            assert_matches_type(AlbumListResponse, album, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_songs(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        album = await async_client.albums.retrieve_songs(
            0,
        )
        assert_matches_type(AlbumRetrieveSongsResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_songs(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        response = await async_client.albums.with_raw_response.retrieve_songs(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album = await response.parse()
        assert_matches_type(AlbumRetrieveSongsResponse, album, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_songs(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        async with async_client.albums.with_streaming_response.retrieve_songs(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album = await response.parse()
            assert_matches_type(AlbumRetrieveSongsResponse, album, path=["response"])

        assert cast(Any, response.is_closed) is True
