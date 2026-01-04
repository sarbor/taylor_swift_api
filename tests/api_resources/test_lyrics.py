# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from taylorswiftlyricsapi import Taylorswiftlyricsapi, AsyncTaylorswiftlyricsapi
from taylorswiftlyricsapi.types import LyricListResponse, LyricRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLyrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Taylorswiftlyricsapi) -> None:
        lyric = client.lyrics.retrieve(
            0,
        )
        assert_matches_type(LyricRetrieveResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Taylorswiftlyricsapi) -> None:
        response = client.lyrics.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lyric = response.parse()
        assert_matches_type(LyricRetrieveResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Taylorswiftlyricsapi) -> None:
        with client.lyrics.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lyric = response.parse()
            assert_matches_type(LyricRetrieveResponse, lyric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Taylorswiftlyricsapi) -> None:
        lyric = client.lyrics.list()
        assert_matches_type(LyricListResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Taylorswiftlyricsapi) -> None:
        lyric = client.lyrics.list(
            number_of_paragraphs=1,
            should_randomize_lyrics=None,
        )
        assert_matches_type(LyricListResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Taylorswiftlyricsapi) -> None:
        response = client.lyrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lyric = response.parse()
        assert_matches_type(LyricListResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Taylorswiftlyricsapi) -> None:
        with client.lyrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lyric = response.parse()
            assert_matches_type(LyricListResponse, lyric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLyrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        lyric = await async_client.lyrics.retrieve(
            0,
        )
        assert_matches_type(LyricRetrieveResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        response = await async_client.lyrics.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lyric = await response.parse()
        assert_matches_type(LyricRetrieveResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        async with async_client.lyrics.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lyric = await response.parse()
            assert_matches_type(LyricRetrieveResponse, lyric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        lyric = await async_client.lyrics.list()
        assert_matches_type(LyricListResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        lyric = await async_client.lyrics.list(
            number_of_paragraphs=1,
            should_randomize_lyrics=None,
        )
        assert_matches_type(LyricListResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        response = await async_client.lyrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lyric = await response.parse()
        assert_matches_type(LyricListResponse, lyric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaylorswiftlyricsapi) -> None:
        async with async_client.lyrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lyric = await response.parse()
            assert_matches_type(LyricListResponse, lyric, path=["response"])

        assert cast(Any, response.is_closed) is True
