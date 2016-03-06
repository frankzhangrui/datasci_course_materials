
import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1], 'r')
    # construct an initial dict
    newdict = {}
    for line in tweet_file:
        data = json.loads(line)
        if "tweet" in line:
            tweet = line["text"]
            for word in re.findall(r'\b([a-z]+)\b',tweet,re.IGNORECASE):
                if word not in newdict:
                    newdict[word] = 1
                else:
                    newdict[word] += 1
    sumall = sum(newdict.values())
    for word in newdict:
        newdict[word] = newdict[word] / float(sumall)
        print word+" ", newdict[word]

if __name__ == '__main__':
    main()