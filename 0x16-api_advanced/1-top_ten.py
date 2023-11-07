#!/usr/bin/python3
"""Ths script will  print the top posts from a subreddit."""
import requests as reqs


def top_ten(subreddit):
    """This method will print the titles of the 10 posts from a subreddit."""
    uri = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
        "limit": 10
    }
    response = reqs.get(uri, headers=headers, parameters=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
