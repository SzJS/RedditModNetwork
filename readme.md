# RedditModNetwork
## What is this?
The point of this project was to create a network representing the connections of the mods of the default subreddits of reddit. In my definition, two moderators are connected if they moderate a shared subreddit (this subreddit doesn't need to be a default, however).
## Where can I find the result?
The graph visualizing the network is in the `result_Sept_10_2016` folder (in both .svg and .gexf file formats). The file was created on the 10th of September 2016, so it is representative of that state of reddit.

There also exists an interactive version of the graph on the [github pages of this project](https://szjs.github.io/RedditModNetwork/).
## How was this graph created?
I used `defaultmods.py` to find all the default subreddits and their moderators, then this result was printed to a file. I then created a .cvs file containing the connections of the mods based on the previouisly mentioned file and the script `create_cvs.py`. Then, I used *gephi* to create the actual graph, and *Sigma js* to create the interactive version.
## Where are the science subreddits?
The science subreddits (/r/science and /r/askscience) were ignored on purpose as they had too many moderators and my computer simple couldn't handle the additional million edges they added to the graph (the final graph has only about 22,000 edges, in comparison).
## Where is AutoModerator?
Just like the science subreddit, AutoModerator had too many connections and thus would have cluttered the graph.
# What does `find_influential.py` do?
I have figured that one simplistic measure of influence is the number of connections a moderator has, so `find_influential.py` ranks the default mods based on their number of connections and writes the result to a file.
