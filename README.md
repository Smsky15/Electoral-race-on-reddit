Electoral Race on Reddit

This year's electoral race has been discussed extensively on Reddit, an online forum that calls itself "the front page of the internet". Having a look in the relation between topics, communities and Redditors is going to enhance a political understanding of the race for the presidency 

With PRAW, a Python wrapper for the Reddit API, we have a tool to pull data and explore the following questions:

- Do Redditors contribute to “hot topics” across the subreddits?
This will be the first step to find data across subreddits and find links between subreddits.

- What are the differences in “hot topics” across the political spectrum? 
This will require us to make a heatmap of keywords used in each subreddit. 

- What are the most controversial topics within each community? 
This will require us to define controversial, perhaps in terms of the ratio of positive to negative comments to a post. Defining this will require us to look into keywords in each comment to label them as positive or negative.

- How does sentiment differ towards hot topics which transcend subreddits? 
This will require us to use the answer to the first question to identify overlapping hot topics, and then do a sentiment analysis of the comments on each related topics.

- Have there been topics which “bled” from one community into another? 
We will have to make timelines of hot topics which became popular across subreddits, to see if some became popular in one subreddit and then, consequently, rose in another. 
