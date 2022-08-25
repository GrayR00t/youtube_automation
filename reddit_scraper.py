'''
#importing 
import praw
import pandas as pd
from praw.models import MoreComments


pd.set_option('max_colwidth', None)

#setting redit api app to fetch the post and comment 
reddit = praw.Reddit(client_id='wmwL_4qi3KBbY7MZSZGViw', client_secret='yXIR7rh2WmQmCtZlk2H1Y8l1m7XJlQ', user_agent='Redit WebScraping')

#fetching posts
posts = []
subreddit = reddit.subreddit('confessions')
for post in subreddit.top(limit = 1):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created , post.upvote_ratio, post.ups, post.downs])


posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'upvote_ratio' ,'up', 'down' ])

body = list(posts['body'])

for post in body:
    print(post)


'''

def get_text(topic):
    #importing 
    import praw
    import pandas as pd
    from praw.models import MoreComments


    pd.set_option('max_colwidth', None)

    #setting redit api app to fetch the post and comment 
    reddit = praw.Reddit(client_id='wmwL_4qi3KBbY7MZSZGViw', client_secret='yXIR7rh2WmQmCtZlk2H1Y8l1m7XJlQ', user_agent='Redit WebScraping')

    #fetching posts
    posts = []
    subreddit = reddit.subreddit(topic)
    for post in subreddit.top(limit = 1):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created , post.upvote_ratio, post.ups, post.downs])


    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'upvote_ratio' ,'up', 'down' ])

    body = list(posts['body'])
    titles = list(posts['title'])
    post_body =""
    post_title=""
    for post in body:
        post_body = post
        break

    for title in titles:
        post_title = title
        break

    return (post_title, post_body)    