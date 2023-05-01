import praw
from key_content import query_keywords

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


posts = search_posts(subreddit_name, query_keywords, limit)

for post in posts:
    print(f'Title: {post.title}')
    print(f'URL: {post.url}\n')
