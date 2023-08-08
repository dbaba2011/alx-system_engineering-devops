#!/usr/bin/python3
"""
Module to recursively retrieve titles of all hot articles in a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieve titles of all hot articles in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles (default is an empty list).
        after (str): ID of the post after which to continue pagination.

    Returns:
        list: List of titles of hot articles, or None if no results are found.
    """
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                return hot_list

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        except (KeyError, ValueError):
            return None
    else:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            for title in result:
                print(title)
        else:
            print("None")
