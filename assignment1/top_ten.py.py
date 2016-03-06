
import sys
import json
from collections import Counter

def main():
    tweet_file = open(sys.argv[1], 'r')
    # construct an initial dict
    newdict = Counter()
    for line in tweet_file:
        try:
            line = json.loads(line)
            hashtags = line['entities']['hashtags']
            for hashtag in hashtags:
                tag = hashtag["text"]
                newdict[tag] += 1
        except:
            pass
    for item in newdict.most_common(10):
        print item[0]+" ", item[1]

if __name__ == '__main__':
    main()