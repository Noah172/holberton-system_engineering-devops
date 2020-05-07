#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given print 0.
"""
import requests
from sys import argv


def top_ten(subreddit):
    reddit = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(reddit, headers=headers, allow_redirects=False)
    if str(response) != "<Response [200]>":
        print("None")
        return
    res_json = response.json()
    top = 0
    hot = res_json['data']['children']
    while top < 10:
        hottes = hot[top]['data']['title']
        print(hottes)
        top += 1
