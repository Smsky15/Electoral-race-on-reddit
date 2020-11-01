#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:15:26 2020

@author: simonwanka
"""


import praw
import pandas as pd



# setting up praw

r = praw.Reddit(client_id= "XXXXX",
                client_secret= "XXXXX",
                user_agent= "XXXXX",
                username= "XXXXX",
                password= "XXXXX")
                
print(r.user.me())

#exploring subreddit
        
# get 10 hot posts from the r/Politics subreddit
hot_posts = r.subreddit('politics').hot(limit=10)
for post in hot_posts:
    print(post.title)
    
#iterate  10 hot posts fromt the r/Politics subreddit

posts = []
ml_subreddit = r.subreddit('politics')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title','score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)

dfpolTop10 = pd.DataFrame(posts)
dfpolTop10 

dfpolTop10.title.value_counts()

    