#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:04:06 2020

@author: simonwanka
"""

from wordcloud import WordCloud
import pandas as pd 
import re


df = pd.read_csv("Top 100 Anarchism.csv")
print(df)

df.head()


# Load the regular expression library

# Remove punctuation
df['title'] = df['title'].map(lambda x: re.sub('[,\.!?]', '', x))
# Convert the titles to lowercase
df['title'] = df['title'].map(lambda x: x.lower())

df.to_csv("clean.csv")


# Join the different processed titles together.
long_string = ','.join(list(df['title'].values))

# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')

# Generate a word cloud
wordcloud.generate(long_string)

# Visualize the word cloud
wordcloud.to_image()


