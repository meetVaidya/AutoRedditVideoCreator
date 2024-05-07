import praw
import json

reddit = praw.Reddit(client_id='Gx3mUcqU7HgYCokSJXZ8ag',
                     client_secret='dosn4nxBd8sMJ792_D2YbyddU4J9OA',
                     user_agent='your_user_agent')

# Specify the subreddit name
subreddit_name = 'AITAH'

# Get the subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Get the top 10 posts from the subreddit
top_posts = subreddit.hot(limit=10)

content_dict = {}

for post in top_posts:
    content_dict[post.id] = {
        'title': post.title,
        'selftext': post.selftext
    }

with open('output.json', 'w') as f:
    json.dump(content_dict, f)