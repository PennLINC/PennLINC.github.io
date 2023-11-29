"""Load and sort wordlist file."""
with open("wordlist.txt", "r") as fo:
    data = fo.readlines()

data = sorted(list(set(data)))

with open("wordlist.txt", "w") as fo:
    fo.write("".join(data))
