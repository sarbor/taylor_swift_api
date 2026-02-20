# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from taylorswiftlyricsapi import Taylorswiftlyricsapi, AsyncTaylorswiftlyricsapi
from taylorswiftlyricsapi.types import SongListResponse, SongRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSongs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Taylorswiftlyricsapi) -> None:
        song = client.songs.retrieve(
            0,
        )
        assert_matches_type(SongRetrieveResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Taylorswiftlyricsapi) -> None:
        response = client.songs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = response.parse()
        assert_matches_type(SongRetrieveResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Taylorswiftlyricsapi) -> None:
        with client.songs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = response.parse()
            assert_matches_type(SongRetrieveResponse, song, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Taylorswiftlyricsapi) -> None:
        song = client.songs.list()
        assert_matches_type(SongListResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Taylorswiftlyricsapi) -> None:
        response = client.songs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = response.parse()
        assert_matches_type(SongListResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Taylorswiftlyricsapi) -> None:
        with client.songs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = response.parse()
            assert_matches_type(SongListResponse, song, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSongs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        song = await async_client.songs.retrieve(
            0,
        )
        assert_matches_type(SongRetrieveResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        response = await async_client.songs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = await response.parse()
        assert_matches_type(SongRetrieveResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        async with async_client.songs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = await response.parse()
            assert_matches_type(SongRetrieveResponse, song, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        song = await async_client.songs.list()
        assert_matches_type(SongListResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        response = await async_client.songs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = await response.parse()
        assert_matches_type(SongListResponse, song, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        async with async_client.songs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = await response.parse()
            assert_matches_type(SongListResponse, song, path=["response"])

        assert cast(Any, response.is_closed) is True
