with open("result.cvs", mode="w", encoding="utf-8") as result:
    result.write("Source;Target;\n")
    with open("mods.txt", encoding="utf-8") as mods:
        lines = mods.readlines()
        for i in range(0, len(lines), 2):
            mod = lines[i].rstrip()
            subreddits = lines[i+1].rstrip().split(" ")
            subreddits = [x for x in subreddits if x != "/r/science" and x != "/r/askscience"]
            # these two subreddits are an anomaly in terms of moderators so they had to be removed
            for j in range(i+2, len(lines), 2):
                another_mod = lines[j].rstrip()
                another_subreddits = lines[j+1].rstrip().split(" ")
                another_subreddits = [x for x in another_subreddits if x != "/r/science" and x != "/r/askscience"]
                if not set(subreddits).isdisjoint(another_subreddits):
                    result.write("{};{};\n".format(mod, another_mod))