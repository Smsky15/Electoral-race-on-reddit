#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:43:24 2020

@author: simonwanka
"""

import praw
import datetime
import pandas as pd



# setting up praw

r = praw.Reddit(client_id= "XXXXX",
                client_secret= "XXXXX",
                user_agent= "XXXXX",
                username= "XXXXX",
                password= "XXXXX")
                
print(r.user.me())

#exploring subreddit
        

for submission in r.subreddit('politics').top('year',limit=100):
    d = {}
    d['id'] = submission.id
    d['title'] = submission.title
    d['num_comments'] = submission.num_comments
    d['score'] = submission.score
    d['upvote_ratio'] = submission.upvote_ratio
    d['date'] = datetime.datetime.fromtimestamp(submission.created)
    d['domain'] = submission.domain
    d['gilded'] = submission.gilded
    d['num_crossposts'] = submission.num_crossposts
    d['nsfw'] = submission.over_18
    d['author'] = submission.author.name
    submission_stats.append(d)
 

dfpolTop100 = pd.DataFrame(submission_stats_pol)
dfpolTop100 

dfpolTop100.author.value_counts()
