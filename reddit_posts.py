import praw
import os
import json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Specify the subreddit name
subreddit_name = 'AITAH'

# Get the subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Get the top 10 posts from the subreddit
top_posts = list(subreddit.hot(limit=11))[1:]

content_dict = {}

for post in top_posts:
    content_dict[post.id] = {
        'title': post.title,
        'selftext': post.selftext,
        'upvotes': post.score,
        'comments' : post.num_comments,
    }
# print(json.dumps(content_dict, indent=4))

