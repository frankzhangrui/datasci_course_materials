import sys
import json

def trans2Dict(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def printScore(scores,tweet_file):
    for line in tweet_file:
        try:
            line = json.loads(line)
            text = line["text"] if "text" in line else ""
            if text != "":
                text = text.strip().split(" ")
                score = sum(map(lambda x: scores[x] if x in scores else 0, text))
                print score
            else:
                print 0
        except:
            print 0

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = trans2Dict(sent_file)
    printScore(scores,tweet_file)

if __name__ == '__main__':
    main()
