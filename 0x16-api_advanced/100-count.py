#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after=None):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    """
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json()["data"]
    after = data.get("after")
    for post in data.get("children"):
        title = post.get("data").get("title").lower()
        for word in word_list:
            if f" {word.lower()} " in f" {title} ":
                if word not in instances:
                    instances[word] = 0
                instances[word] += title.count(f" {word.lower()} ")

    if after is not None:
        count_words(subreddit, word_list, instances, after)

    if not instances:
        return

    sorted_instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_instances:
        print(f"{word.lower()}: {count}")
