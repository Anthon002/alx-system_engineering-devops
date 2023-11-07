#!/usr/bin/python3
"""this script will query a list of all top posts from a  subreddit."""
import requests as reqs


def recurse(subreddit, top_list=[], after="", count=0):
    """This method returns a list of titles of all top posts from a subreddit."""
    uri = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = reqs.get(uri, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    _res = response.json().get("data")
    after = _res.get("after")
    count += _res.get("dist")
    for c in _res.get("children"):
        top_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, top_list, after, count)
    return top_list
