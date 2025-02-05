"""Function to summarise the top_n sentiments from a list of call events."""

from typing import List

def top_sentiments(events: List[dict], top_n: int, customer_id: str) -> List[str]:
    """
    Takes in a list of call events and returns the top_n sentiments of a customer

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
                }
            ]

    :param top_n: Number of sentiments to return
    :param customer_id: The string of customer id

    :return: List of top_n sentiments
        Examples:
            >>> top_sentiments(events, 2, "a")
            ['bored', 'happy']
    """
    raise NotImplementedError()
