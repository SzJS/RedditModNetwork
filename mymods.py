import getpass
import requests
import requests.auth
import time
from secret import secret
from shared import version_string

pswd = getpass.getpass('Password:')
client_auth = requests.auth.HTTPBasicAuth('BNt88FhRgC1OsQ', secret)
post_data = {"grant_type": "password", "username": "Thessalonican17", "password": pswd}
headers = {"User-Agent": "modsaregods/{} by Thessalonican17".format(version_string)}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
access_token = response.json()["access_token"]
headers = {"Authorization": "bearer " + access_token, "User-Agent": "modsaregods/{} by Thessalonican17".format(version_string)}
response = requests.get("https://oauth.reddit.com/subreddits/mine/subscriber?limit=50", headers=headers)
# the limit is 50 so that the application doesn't exceed 60 requests per minute

raw_subreddits = response.json()["data"]["children"]
subreddits = []
for subreddit in raw_subreddits:
    subreddits.append(subreddit["data"]["display_name"])

mods = dict()
for subreddit in subreddits:
    response = requests.get("https://oauth.reddit.com/r/{}/about/moderators".format(subreddit), headers=headers)
    raw_mods = response.json()["data"]["children"]
    for raw_mod in raw_mods:
        mod = raw_mod["name"]
        if mod in mods.keys():
            mods[mod] += 1
        else:
            mods[mod] = 1

for mod, number in mods.items():
    if number > 1:
        print("{} moderates {} subreddits".format(mod, number))