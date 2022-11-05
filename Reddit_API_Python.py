import time
import praw

reddit = praw.Reddit(client_id ='6TjAobShVL80ZGA7sIkqAg',
                     client_secret ='eM09qgJQeklbVrkea6vEq6PBHNGhWQ',
                     user_agent =':)',
                     username ='EstablishmentFit9892',
                     password ='V1h@@n1s@R0b0t')
 
# to verify whether the instance is authorized instance or not

subreddit = reddit.subreddit('AskReddit')

hot_python = subreddit.hot(limit=30)
for submission in hot_python:
    if not submission.stickied:
        print('Title: {}'.format(submission.title))
        comments = submission.comments
        for comment in comments:
            print(20*'-')
            print(comment.body)