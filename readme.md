# RedditModNetwork
## What is this?
This is just a small project that I did to learn a bit about reddit API and reddit's moderator network. I used `defaultmods.py` to find all the default subreddits and their moderators, then this result was printed to a file. I then created a .cvs file containing the connections of the mods based on the previouisly mentioned file and the script `create_cvs.py`. Then, I used *gephi* to create the actual graph.
## Where are the results?
The result is in the `result_Sept_10_2016` folder (in both .svg and .gexf file formats). The file was created on the 10th of September 2016, so it is a representation of that state of reddit.

There also exists an interactive version of the graph on the [github pages of this project](https://szjs.github.io/RedditModNetwork/).
## Where are the science subreddits?
The science subreddits (/r/science and /r/askscience) were ignored on purpose as they had too many moderators and my computer simple couldn't handle the additional million edges they added to the graph (the final graph has only about 22,000 edges, in comparison).
## Where is AutoModerator?
Just like the science subreddit, AutoModerator had too many connections and thus would have cluttered the graph. Furthermore, AutoModerator is a bot, so his exclusion does not make the graph less accurate.
