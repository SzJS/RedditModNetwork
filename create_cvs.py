with open("result.cvs", mode="w", encoding="utf-8") as result:
    result.write("Source;Target;\n")
    with open("mods.txt", encoding="utf-8") as mods:
        lines = mods.readlines()
        for i in range(0, len(lines), 2):
            mod = lines[i].rstrip()
            subreddits = lines[i+1].rstrip().split(" ")
            for j in range(i+2, len(lines), 2):
                another_mod = lines[j].rstrip()
                another_subreddits = lines[j+1].rstrip().split(" ")
                if set(subreddits).isdisjoint(another_subreddits):
                    result.write("{};{};\n".format(mod, another_mod))