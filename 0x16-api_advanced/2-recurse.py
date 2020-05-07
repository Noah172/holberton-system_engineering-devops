#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given print 0.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if str(response) != '<Response [200]>':
        return None
    res_json = response.json()
    posts = response.json()['data']['dist']  # Number of posts on page
    index = 0
    inf = res_json['data']['children']  # Dict of posts
    while index < posts:
        data = inf[index]['data']['title']
        hot_list.append(data)
        index += 1
    after = res_json['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
