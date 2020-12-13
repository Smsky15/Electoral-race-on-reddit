#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:23:40 2020

@author: simonwanka
"""
import praw
from textblob import TextBlob
import nltk #Download the VADAR tool and access it through the NLTK library

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# create object for VADER sentiment function interaction
sia = SentimentIntensityAnalyzer()

r = praw.Reddit(client_id= "94J5DUz2HFhkCw",
                client_secret= "fcdwbW815czCBnyQYxOMPFOTcDqYew",
                user_agent= "u/smsky15",
                username= "smsky15",
                password= "Zef21286637?")
                
print(r.user.me())

# hot topics from the subreddit _ only the whole year
top_posts = r.subreddit("Anarchism").top("year", limit=5)

# sentiment analysis function TextBlob 
def text_blob_sentiment(review, sub_entries_textblob):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity >= 0.0001:
        if analysis.sentiment.polarity > 0:
            sub_entries_textblob['positive'] = sub_entries_textblob['positive'] + 1
            return 'Positive'

    elif analysis.sentiment.polarity <= -0.0001:
        if analysis.sentiment.polarity <= 0:
            sub_entries_textblob['negative'] = sub_entries_textblob['negative'] + 1
            return 'Negative'
    else:
        sub_entries_textblob['neutral'] = sub_entries_textblob['neutral'] + 1
        return 'Neutral'
    

# sentiment analysis function VADER 
def nltk_sentiment(review, sub_entries_nltk):
    vs = sia.polarity_scores(review)
    if not vs['neg'] > 0.05:
        if vs['pos'] - vs['neg'] > 0:
            sub_entries_nltk['positive'] = sub_entries_nltk['positive'] + 1
            return 'Positive'
        else:
            sub_entries_nltk['neutral'] = sub_entries_nltk['neutral'] + 1
            return 'Neutral'

    elif not vs['pos'] > 0.05:
        if vs['pos'] - vs['neg'] <= 0:
            sub_entries_nltk['negative'] = sub_entries_nltk['negative'] + 1
            return 'Negative'
        else:
            sub_entries_nltk['neutral'] = sub_entries_nltk['neutral'] + 1
            return 'Neutral'
    else:
        sub_entries_nltk['neutral'] = sub_entries_nltk['neutral'] + 1
        return 'Neutral'


# replication of comment section
def replies_of(top_level_comment, count_comment, sub_entries_textblob, sub_entries_nltk):
    if len(top_level_comment.replies) == 0:
        count_comment = 0
        return
    else:
        for num, comment in enumerate(top_level_comment.replies):
            try:
                count_comment += 1
                print('-' * count_comment, comment.body)
                text_blob_sentiment(comment.body, sub_entries_textblob)
                nltk_sentiment(comment.body, sub_entries_nltk)
            except:
                continue
            replies_of(comment, count_comment, sub_entries_textblob,sub_entries_nltk)


def main():
    
    for submission in top_posts:
        sub_entries_textblob = {'negative': 0, 'positive' : 0, 'neutral' : 0}
        sub_entries_nltk = {'negative': 0, 'positive' : 0, 'neutral' : 0}
        print('Title of the post :', submission.title)
        text_blob_sentiment(submission.title, sub_entries_textblob)
        nltk_sentiment(submission.title, sub_entries_nltk)
        print("\n")
        submission_comm = r.submission(id=submission.id)

        for count, top_level_comment in enumerate(submission_comm.comments):
            print(f"-------------{count} top level comment start--------------")
            count_comm = 0
            try :
                print(top_level_comment.body)
                text_blob_sentiment(top_level_comment.body, sub_entries_textblob)
                nltk_sentiment(top_level_comment.body, sub_entries_nltk)
                replies_of(top_level_comment,
                           count_comm,
                           sub_entries_textblob,
                           sub_entries_nltk)
            except:
                continue
        print('Over all Sentiment of Topic by TextBlob :', sub_entries_textblob)
        print('Over all Sentiment of Topic by VADER :', sub_entries_nltk)
        print("\n\n\n")

if __name__ == '__main__' :
    main()