#!/usr/bin/python3
"""This script will to return top posts from a subreddit."""
import requests as reqs


def top_ten(subreddit):
    """This method will return the titles of the 10 top posts on a subreddit."""
    uri = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameter = {
        "limit": 10
    }
    response = reqs.get(uri, headers=headers, parameter=parameter,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    _res = response.json().get("data")
    [print(c.get("data").get("title")) for c in _res.get("children")]
