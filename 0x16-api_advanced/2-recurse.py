#!/usr/bin/python3
""" this script will query a list of all top posts from a subreddit."""
import requests as reqs


def recurse(subreddit, hot_list=[], after="", count=0):
    """this method will returns a list of titles of all top posts from a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = reqs.get(url, headers=headers, parameters=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    _result = response.json().get("data")
    after = _result.get("after")
    count += _result.get("dist")
    for c in _result.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
