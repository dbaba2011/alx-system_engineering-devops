#!/usr/bin/python3
"""
Get number of subscribers for the subreddit
"""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # Construct the API URL for the subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            
            return subscribers
        except (KeyError, ValueError):
            # Invalid JSON response or missing data
            return 0
    else:
        # Invalid subreddit or other error
        return 0

# Test the function
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
