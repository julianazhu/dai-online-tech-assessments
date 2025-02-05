"""Test the sentiment summarizing function"""

import json
from typing import List

import pytest

from sentiment import top_sentiments


@pytest.fixture(scope="class")
def events() -> dict:
    """
    Fixture to return a series of events
    """
    return [
        {
            "customer_id": "a",
            "call_id": 1,
            "sentiments": ["happy", "sad", "bored"],
        },
        {
            "customer_id": "a",
            "call_id": 2,
            "sentiments": ["happy", "bored", "sleepy"],
        },
        {
            "customer_id": "a",
            "call_id": 3,
            "sentiments": ["doubtful", "happy"],
        },
        {
            "customer_id": "b",
            "call_id": 4,
            "sentiments": ["bored"],
        },
    ]


@pytest.mark.usefixtures("events")
class TestSentiment:
    """
    Tests for the sentiment summarizing function
    """

    def test_top_sentiments_with_valid_input(self, events: List[str]):
        """
        Test to see if the function returns the correct top_n sentiments
        when given a valid input
        """
        assert top_sentiments(events, top_n=2, customer_id="a") == ["happy", "bored"]
