# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:26:55 2020

@author: guill
"""

import pandas as pd 
import matplotlib.pyplot as plt

#importing the dataframe for every subreddit

megadf = pd.read_csv('megadata_csv.csv')

anardf = pd.read_csv('Top 100 Anarchism.csv')

anarcapdf = pd.read_csv('Top 100 Anarcho_Capitalism.csv')

conserdf = pd.read_csv('Top 100 Conservative.csv')

demdf = pd.read_csv('Top 100 democrats.csv')

trumpdf = pd.read_csv('Top 100 donaldtrump.csv')

greendf = pd.read_csv('Top 100 GreenParty.csv')

bidendf = pd.read_csv('Top 100 JoeBiden.csv')

liberdf = pd.read_csv('Top 100 Libertarian.csv')

progdf = pd.read_csv('Top 100 progressive.csv')

repudf = pd.read_csv('Top 100 Republican.csv')

socialdf = pd.read_csv('Top 100 socialism.csv')

#Pulling the most controversial hot topic of each subreddit, by selecting the row that corresponds to the lowest upvote_ratio

topconmega = megadf.loc[megadf['upvote_ratio'].idxmin()]

contranar = anardf.loc[anardf['upvote_ratio'].idxmin()]

contranarcap = anarcapdf.loc[anarcapdf['upvote_ratio'].idxmin()]

contrcons = conserdf.loc[conserdf['upvote_ratio'].idxmin()]

contrdem = demdf.loc[demdf['upvote_ratio'].idxmin()]

contrtrump = trumpdf.loc[trumpdf['upvote_ratio'].idxmin()]

contrgreen = greendf.loc[greendf['upvote_ratio'].idxmin()]

contrbiden = bidendf.loc[bidendf['upvote_ratio'].idxmin()]

contrliber = liberdf.loc[liberdf['upvote_ratio'].idxmin()]

contrprog = progdf.loc[progdf['upvote_ratio'].idxmin()]

contrepub = repudf.loc[repudf['upvote_ratio'].idxmin()]

contrsoc = socialdf.loc[socialdf['upvote_ratio'].idxmin()]

#Creating a dataframe with the average upvote ratio for each subreddit, and the 
#upvote_ratio of the most controversial post
upvoteratio = {'Subreddit': ['Anarchists','Socialists','Greens','Progressives', 
                             'Democrats', 'Biden supporters', 'Libertarians',
                             'Conservatives', 'Republicans','Anarcho-Capitalists', 
                             'Trump supporters'],
        'Average upvote ratio': [anardf["upvote_ratio"].mean(),socialdf["upvote_ratio"].mean(),
        greendf["upvote_ratio"].mean(), progdf["upvote_ratio"].mean(), demdf["upvote_ratio"].mean(),
        bidendf["upvote_ratio"].mean(), liberdf["upvote_ratio"].mean(), 
        conserdf["upvote_ratio"].mean(), repudf["upvote_ratio"].mean(),
        anarcapdf["upvote_ratio"].mean(), trumpdf["upvote_ratio"].mean()],
        
        'Most controversial submission': [contranar['upvote_ratio'], contrsoc['upvote_ratio'],
                                          contrgreen['upvote_ratio'], contrprog['upvote_ratio'],
                                          contrdem['upvote_ratio'], contrbiden['upvote_ratio'],
                                          contrliber['upvote_ratio'], contrcons['upvote_ratio'],
                                          contrepub['upvote_ratio'], contranarcap['upvote_ratio'],
                                          contrtrump['upvote_ratio']]
        }

upvotedf = pd.DataFrame(upvoteratio, columns = ['Subreddit','Average upvote ratio', 'Most controversial submission'], index=['Anarchists','Socialists','Greens','Progressives', 
                             'Democrats', 'Biden supporters', 'Libertarians',
                             'Conservatives', 'Republicans','Anarcho-Capitalists', 
                             'Trump supporters'])

upvotedf.to_csv( "upvotedf.csv", index=False, encoding='utf-8-sig')


ax = plt.gca()

upvotedf.plot(kind='line',x='Subreddit',y='Average upvote ratio',ax=ax)
upvotedf.plot(kind='line',x='Subreddit',y='Most controversial submission', color='red', ax=ax)
plt.ylabel('Upvote ratio')
plt.xlabel('Subreddit')
plt.xticks(range(0,len(upvotedf.index)), upvotedf['Subreddit'], rotation=60)
fig = plt.gcf()
fig.set_size_inches(10, 7, forward=True)
plt.tight_layout()
plt.savefig('fig1.png', dpi = 100)
plt.show()

