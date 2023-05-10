#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom User"}

    params = {"limit": 1, "after": after}
    res = requests.get(
              url, headers=headers, params=params, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data").get("children")
        hot_list.append(data[0].get("data").get("title"))

        after = res.json().get("data").get("after")
        recurse(subreddit, hot_list, after)
    else:
        return None

    return hot_list
