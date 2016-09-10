import getpass
import requests
import requests.auth
import pyquery
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

with open("mods.txt", mode="w", encoding="utf-8") as file:
    for mod in mods:
        file.write(mod + "\n")
        time.sleep(1)
        response = requests.get("https://reddit.com/user/{}/".format(mod), headers=headers)
        pq = pyquery.PyQuery(response.content)
        for subreddit in [x.text for x in pq("#side-mod-list li a")]:
            file.write(subreddit + " ")
        file.write("\n")