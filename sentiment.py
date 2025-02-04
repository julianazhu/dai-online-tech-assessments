"""Function to summarise the top_n sentiments from a list of call events."""

import json
from typing import List


def top_sentiments(events: List[dict], top_n: int, n: int) -> list:
    """
    Takes in a list of call events and returns the top_n sentiments of the last n calls by frequency.

    :param events: List of events
        Example:
            [
                {
                    "customer_id": "a",
                    "call_id": 1,
                    "sentiments": [
                        "happy",
                        "sad",
                        "bored"
                    ],
                    "timestamp": "2024-10-01T12:00:00Z"
                }
            ]

    :param top_n: Number of sentiments to return
    :param x: The number of calls to consider

    :return: List of top_n sentiments
        Examples:
            >>> top_sentiments(2, 3)
            ['bored', 'happy']
    """
    raise NotImplementedError()
