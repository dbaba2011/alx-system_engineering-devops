#!/usr/bin/python3
"""
Module to print the titles of the first 10 hot posts in a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for i, post in enumerate(posts[:10], start=1):
                title = post['data']['title']
                print(title)
        except (KeyError, ValueError):
            print("None")
    else:
        print("None")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
