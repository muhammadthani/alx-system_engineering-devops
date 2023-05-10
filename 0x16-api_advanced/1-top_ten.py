#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom User"}
    params = {"limit": 10}
    res = requests.get(
          url, headers=headers, params=params, allow_redirects=False)
    data = res.json().get("data").get(
           "children") if res.status_code == 200 else None
    if data:
        for _ in data:
            print(_.get("data").get("title"))
    else:
        print(None)
