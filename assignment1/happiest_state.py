import sys
import json
from collections import defaultdict
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def trans2Dict(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def printScore(scores,tweet_file):
    state_scores = {}
    for line in tweet_file:
        try:
            line = json.loads(line)
            text = line["text"] if "text" in line else ""
            if text != "":
                location = line["place"]["full_name"].split(",")
                state = location[1].strip() if len(location) == 2 else ""
                if state in states:
                    summation = sum(map(lambda x: scores[x] if x in scores else 0, text.split(" ")))
                    N = len(text.split(" "))
                    if state not in state_scores:
                        state_scores[state] = {"sum":summation,"len":N}
                    else:
                        state_scores[state]["sum"] += summation
                        state_scores[state]["len"] += N
        except:
            pass
    final_state, rst = "" , -1
    for state, value in state_scores.items():
        average = value["sum"]/float(value["len"])
        if rst < average:
            rst = average
            final_state = state
    print final_state

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = trans2Dict(sent_file)
    printScore(scores,tweet_file)

if __name__ == '__main__':
    main()

