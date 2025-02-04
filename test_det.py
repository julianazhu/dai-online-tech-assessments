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
            "timestamp": "2024-10-01T10:00:00Z",
        },
        {
            "customer_id": "b",
            "call_id": 2,
            "sentiments": ["happy", "bored", "sleepy"],
            "timestamp": "2024-10-01T11:00:00Z",
        },
        {
            "customer_id": "c",
            "call_id": 3,
            "sentiments": ["doubtful", "happy"],
            "timestamp": "2024-10-01T12:00:00Z",
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
        assert top_sentiments(events, top_n=2, n=3) == ["happy", "bored"]
