# -*- coding: utf-8 -*-
import sys
import json
def trans2Dict(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def parseTweet(tweet_file):
    tweets = []
    for line in tweet_file:
        try:
            line = json.loads(line)
            if "text" in line:
                tweets.append(line["text"])
        except:
            pass
    return tweets


def unKnownTerm(tweets, scores):
    unknownScore = {}
    for tweet in tweets:
        words = tweet.strip().split(" ")
        unknown_words = filter(lambda x: x not in scores, words)
        known_words = filter(lambda x: x in scores, words)
        summation = sum(map(lambda word: scores[word], known_words))
        N = len(known_words)
        for unknown_word in unknown_words:
            if unknown_word not in unknownScore:
                unknownScore[unknown_word] = {"sum":summation,"len":N}

            else:
                unknownScore[unknown_word]["sum"] += summation
                unknownScore[unknown_word]["len"] += N

    for unknown_word in unknownScore:
        summation = unknownScore[unknown_word]["sum"]
        N = max(unknownScore[unknown_word]["len"],0.001)
        print unknown_word + " " + str(summation/float(N))
    return


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = trans2Dict(sent_file)
    tweets = parseTweet(tweet_file)
    unKnownTerm(tweets,scores)


if __name__ == '__main__':
    main()
