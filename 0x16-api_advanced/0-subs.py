#!/usr/bin/python3
"""this script will  query subscribers from a  subreddit."""
import requests as req 

def number_of_subscribers(subreddit):
    """This will return  total no. of subs from a given subreddit."""
    uri = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    responses = req.get(uri, headers=headers, allow_redirects=False)
    if responses.status_code == 404:
        return 0
    else:
      results = responses.json().get("data")
      return results.get("subscribers")
