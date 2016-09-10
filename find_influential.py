with open("mods.txt", encoding="utf-8") as mods:
    lines = mods.readlines()
influential = dict()
for i in range(0, len(lines), 2):
    mod = lines[i].rstrip()
    subreddits = lines[i+1].rstrip().split(" ")
    subreddits = [x for x in subreddits if x != "/r/science" and x != "/r/askscience"]
    for j in range(i+2, len(lines), 2):
        another_mod = lines[j].rstrip()
        another_subreddits = lines[j+1].rstrip().split(" ")
        another_subreddits = [x for x in another_subreddits if x != "/r/science" and x != "/r/askscience"]
        if not set(subreddits).isdisjoint(another_subreddits):
            if mod in influential.keys():
                influential[mod] += 1
            else:
                influential[mod] = 1
            if another_mod in influential.keys():
                influential[another_mod] += 1
            else:
                influential[another_mod] = 1
influential = influential.items()
influential = sorted(influential, key=lambda tup: tup[1])
with open("influence.txt", mode="w", encoding="utf-8") as file:
    for (mod, connections) in influential:
        file.write("{} - {}\n".format(mod, connections))