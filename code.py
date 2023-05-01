import praw
from key_content import query_keywords

client_id = '68n97pmuxvLUfkVHxU7w-w'
client_secret = 'bX25ZyAiK9Dg0-h423W5jQkRlDhArw'
user_agent = 'python:islfo:v1.0.0 (by /u/itm448)'
username = 'itm448'
password = 'Chicago12345!'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

def search_posts(subreddit_name, query, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.search(query, limit=limit)

subreddit_name = 'AskReddit'
limit = 10

# Use the query_keywords variable imported from key_content.py
posts = search_posts(subreddit_name, query_keywords, limit)

for post in posts:
    print(f'Title: {post.title}')
    print(f'URL: {post.url}\n')





