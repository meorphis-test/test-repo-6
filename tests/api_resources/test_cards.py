# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_6 import MeorphisTest6, AsyncMeorphisTest6
from meorphis_test_6.types import (
    CardCreateResponse,
    CardUpdateResponse,
    CardRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest6) -> None:
        card = client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest6) -> None:
        card = client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            carrier={"qr_code_url": "string"},
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            shipping_address={
                "first_name": "Michael",
                "last_name": "Bluth",
                "line2_text": "The Bluth Company",
                "address1": "5 Broad Street",
                "address2": "Unit 25A",
                "city": "NEW YORK",
                "state": "NY",
                "postal_code": "10001-1809",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "phone_number": "+12124007676",
            },
            shipping_method="STANDARD",
            spend_limit=1000,
            spend_limit_duration="TRANSACTION",
            state="OPEN",
        )
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest6) -> None:
        response = client.cards.with_raw_response.create(
            type="VIRTUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest6) -> None:
        with client.cards.with_streaming_response.create(
            type="VIRTUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardCreateResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MeorphisTest6) -> None:
        card = client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardRetrieveResponse, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MeorphisTest6) -> None:
        response = client.cards.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardRetrieveResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MeorphisTest6) -> None:
        with client.cards.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardRetrieveResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MeorphisTest6) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: MeorphisTest6) -> None:
        card = client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardUpdateResponse, card, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: MeorphisTest6) -> None:
        card = client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="Updated Name",
            pin="string",
            spend_limit=100,
            spend_limit_duration="FOREVER",
            state="OPEN",
        )
        assert_matches_type(CardUpdateResponse, card, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: MeorphisTest6) -> None:
        response = client.cards.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardUpdateResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: MeorphisTest6) -> None:
        with client.cards.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardUpdateResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: MeorphisTest6) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.update(
                "",
            )


class TestAsyncCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest6) -> None:
        card = await async_client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest6) -> None:
        card = await async_client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            carrier={"qr_code_url": "string"},
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            shipping_address={
                "first_name": "Michael",
                "last_name": "Bluth",
                "line2_text": "The Bluth Company",
                "address1": "5 Broad Street",
                "address2": "Unit 25A",
                "city": "NEW YORK",
                "state": "NY",
                "postal_code": "10001-1809",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "phone_number": "+12124007676",
            },
            shipping_method="STANDARD",
            spend_limit=1000,
            spend_limit_duration="TRANSACTION",
            state="OPEN",
        )
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest6) -> None:
        response = await async_client.cards.with_raw_response.create(
            type="VIRTUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest6) -> None:
        async with async_client.cards.with_streaming_response.create(
            type="VIRTUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardCreateResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMeorphisTest6) -> None:
        card = await async_client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardRetrieveResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMeorphisTest6) -> None:
        response = await async_client.cards.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardRetrieveResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMeorphisTest6) -> None:
        async with async_client.cards.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardRetrieveResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMeorphisTest6) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMeorphisTest6) -> None:
        card = await async_client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardUpdateResponse, card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMeorphisTest6) -> None:
        card = await async_client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="Updated Name",
            pin="string",
            spend_limit=100,
            spend_limit_duration="FOREVER",
            state="OPEN",
        )
        assert_matches_type(CardUpdateResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMeorphisTest6) -> None:
        response = await async_client.cards.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardUpdateResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMeorphisTest6) -> None:
        async with async_client.cards.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardUpdateResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMeorphisTest6) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.update(
                "",
            )
