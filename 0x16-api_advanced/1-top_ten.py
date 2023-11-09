#!/usr/bin/python3
""" top 10 hot posts """
import requests


def top_ten(subreddit):
    """
    query top 10 hot posts
    Args:
        subreddit: name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    header = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {'limit': 10}
    response = requests.get(url, headers=header,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    data = response.json()
    for post in data.get("data", {}).get("children", []):
        print(post.get("data", {}).get("title", ""))
