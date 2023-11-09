#!/usr/bin/python3
""" query on reddit api """

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    Args:
      subreddit: name of the subreddit
    Returns:
      number of subscribers of the subreddit
    """
    url = f"https://reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
