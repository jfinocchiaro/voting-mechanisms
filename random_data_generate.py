import numpy as np
import csv
import random


num_candidates = 4
num_counties   = 20
num_voters = 1000
distribution = 'random-all'

def datagen(num_candidates, num_counties, num_votes, distribution):
    dataset = {}
    if distribution == 'uniform-voters-uniform-candidates':
        candidate_list = range(1, num_candidates+1)
        #voters prefer a candidate with unfiorm probability.  preference order given by shuffling list.
        for i in range(num_voters):
            dataset[i] = {'prefs' : random.shuffle(candidate_list), 'county' : random.randint(1, num_counties)}

    elif distribution == 'uniform-voters-two-horse-race':
        pass

    elif distribution == 'non-uniform-voters-uniform-candidates':
        pass

    elif distribution == 'non-uniform-voters-non-uniform-candidates':
            pass

    else:
        print ('I don\'t know what distribution you want :(')
        quit()

    return dataset

def writeoutput(filename):
    for voter_key, voter_vote in dataset.itervalues():
        pass
        #csv.write()
