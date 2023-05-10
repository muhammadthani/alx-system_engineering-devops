#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom User"}

    res = requests.get(url, headers=headers)
    data = res.json().get("data").get(
           "subscribers") if res.status_code == 200 else 0
    return data
