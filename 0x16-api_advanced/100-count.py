#!/usr/bin/python3
""" model parses the title of all hot articles """


def count_words(subreddit, word_list):
    """
    query the Reddit API, parse the title of all hot articles,
    and print a sorted count of given keywords
    """
    import requests

    url = f"https://reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("")
        return

    data = response.json()
    count = {}
    for post in data.get("data", {}).get("children", []):
        title = post.get("data", {}).get("title", "").lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                count[word] = count.get(word, 0) + 1

    for key, value in sorted(count.items(), key=lambda x: x[1]):
        print("{}: {}".format(key, value))


count_words("programming",
            "react python java javascript scala no_results_for_this_one".split())
