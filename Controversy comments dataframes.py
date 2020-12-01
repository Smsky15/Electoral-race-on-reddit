# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:55:10 2020

@author: guill
"""

import praw
import pandas as pd

# setting up praw

r = praw.Reddit(client_id= "94J5DUz2HFhkCw",
                client_secret= "fcdwbW815czCBnyQYxOMPFOTcDqYew",
                user_agent= "u/Fistulin",
                username= "Fistulin",
                password= "jppMDR363!!!")

#Extracting comments from the socialist controversy

socsub = r.submission(id='fmuozp')

socsub.comments.replace_more(limit=None)

#creating a dictionary
getsocdic = { "id":[],
             "body":[] }


for comment in socsub.comments.list():
    getsocdic["id"].append(comment.id)
    getsocdic["body"].append(comment.body)
    
getsocdf = pd.DataFrame(getsocdic)

getsocdf.to_csv("socialcon.csv")

#Extracting comments from the Biden controversy

bidsub = r.submission(id='i7zagl')

bidsub.comments.replace_more(limit=None)

#creating a dictionary
getbiddic = { "id":[],
             "body":[] }


for comment in socsub.comments.list():
    getbiddic["id"].append(comment.id)
    getbiddic["body"].append(comment.body)
    
getbiddf = pd.DataFrame(getbiddic)

getbiddf.to_csv("bidencon.csv")

#Extracting comments from the Libertarian controversy

consub = r.submission(id='haq8cw')

consub.comments.replace_more(limit=None)

#creating a dictionary
getcondic = { "id":[],
             "body":[] }


for comment in consub.comments.list():
    getcondic["id"].append(comment.id)
    getcondic["body"].append(comment.body)
    
getcondf = pd.DataFrame(getcondic)

getcondf.to_csv("libercon.csv")