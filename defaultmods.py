import getpass
import requests
import requests.auth
import pyquery
import time

version_string = "0.1.2"

pswd = getpass.getpass('Password:')
client_auth = requests.auth.HTTPBasicAuth('BNt88FhRgC1OsQ', 'pgnkTeR6ZvV5dT9MiPCKPxvQoRo')
post_data = {"grant_type": "password", "username": "Thessalonican17", "password": pswd}
headers = {"User-Agent": "modsaregods/{} by Thessalonican17".format(version_string)}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
access_token = response.json()["access_token"]
headers = {"Authorization": "bearer " + access_token, "User-Agent": "modsaregods/{} by Thessalonican17".format(version_string)}
response = requests.get("https://oauth.reddit.com/subreddits/default?limit=50", headers=headers)

raw_subreddits = response.json()["data"]["children"]
defaults = []
for subreddit in raw_subreddits:
    defaults.append(subreddit["data"]["display_name"])

mods = set()
for default in defaults:
    time.sleep(1)
    response = requests.get("https://oauth.reddit.com/r/{}/about/moderators".format(default), headers=headers)
    raw_mods = response.json()["data"]["children"]
    for raw_mod in raw_mods:
        mod = raw_mod["name"]
        mods.add(mod)

for mod in mods:
    time.sleep(1)
    response = requests.get("https://reddit.com/user/{}/".format(mod), headers=headers)
    pq = pyquery.PyQuery(response.content)
    number = sum(1 for x in pq("#side-mod-list li a"))
    print("{} moderates {} subreddits".format(mod, number))