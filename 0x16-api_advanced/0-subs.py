#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given return 0.
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    reddit = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(reddit, headers=headers, allow_redirects=False)
    if str(response) != "<Response [200]>":
        return 0
    res_json = response.json()
    subs = res_json.get("data").get("subscribers")
    return subs