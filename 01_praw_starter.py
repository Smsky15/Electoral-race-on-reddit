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
#creating a list with the main topics

                                     
#creating a dictionary
  
topics_dict = { "title":[],
                "score":[],
                "id":[], 
                "url":[],
                "comms_num": [],
                "body":[],
                "author": [],
                "created_utc": [],
                "upvote_ratio":[]} 

#pulling the features together

for submission in r.subreddit("Anarchism").top("year", limit=100):
    before = "1597190400" #August 12th
    after = "1601683200"  #November 3rd
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["body"].append(submission.selftext)  
    topics_dict["author"].append(submission.author)
    topics_dict["created_utc"].append(submission.created_utc)
    topics_dict["upvote_ratio"].append(submission.upvote_ratio)

#the subreddit data
topics_data = pd.DataFrame(topics_dict)

print(topics_data)

#Authors of the top 100
topics_data.author.value_counts()

#creating a dictionary for author
  
author_dict = { "title":[],
                "score":[],
                "id":[], 
                "url":[],
                "comms_num": [],
                "body":[],
                "author": [],
                "created_utc": [],
                "upvote_ratio":[],
                "subreddit":[]} 

#Authors engagement throughout Reddit w more value count more than two
for submission in r.redditor("nahmate45").top("year", limit=10):
    before = "1597190400" #August 12th
    after = "1601683200"  #November 3rd
    author_dict["title"].append(submission.title)
    author_dict["score"].append(submission.score)
    author_dict["id"].append(submission.id)
    author_dict["url"].append(submission.url)
    author_dict["comms_num"].append(submission.num_comments)
    author_dict["body"].append(submission.selftext)  
    author_dict["author"].append(submission.author)
    author_dict["created_utc"].append(submission.created_utc)
    author_dict["upvote_ratio"].append(submission.upvote_ratio)
    author_dict["subreddit"].append(submission.subreddit)
    
author_data=pd.DataFrame(author_dict)
author_data.to_csv("Top Author Anarchism.csv")
print(author_data)

ax=author_data.plot.scatter(x='score',y='comms_num',s=50,c='k',alpha=.5)
