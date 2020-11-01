#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:48:42 2020

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
  
topics_dict = { "title":[],
                "score":[],
                "id":[], 
                "url":[],
                "comms_num": [],
                "created": [],
                "body":[],
                "author": []} 

for submission in r.subreddit('politics').top('month',limit=100):
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)  
    topics_dict["author"].append(submission.author.name)

topics_data = pd.DataFrame(topics_dict)

print(topics_data)

