#!/usr/bin/python3
"""
Module to recursively count keywords in titles of all hot articles in a subreddit
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively count keywords in titles of all hot articles in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): ID of the post after which to continue pagination.
        count_dict (dict): Dictionary to store keyword counts.

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print("{}: {}".format(word, count))
                return

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if title.count(word) > 0:
                        count_dict[word] = count_dict.get(word, 0) + title.count(word)

            after = data['data']['after']
            return count_words(subreddit, word_list, after, count_dict)
        except (KeyError, ValueError):
            return
    else:
        return


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
