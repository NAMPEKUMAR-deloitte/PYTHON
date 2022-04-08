def longest(file):
    with open(file, 'r') as infile:
        wrd = infile.read().split()
    maxLen = len(max(wrd, key=len))
    return [word for word in wrd if len(word) == maxLen]


print(longest('a'))