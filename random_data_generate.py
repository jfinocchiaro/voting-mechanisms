import numpy as np
import csv
import random


num_candidates = 4
num_counties   = 10
num_voters = 1000
distribution = 'uniform-voters-two-horse-race'

def datagen(num_candidates, num_counties, num_voters, distribution):
    dataset = {}
    if distribution == 'uniform-voters-uniform-candidates':

        #voters prefer a candidate with unfiorm probability.  preference order given by shuffling list.
        for i in range(num_voters):
            candidate_list = range(1, num_candidates+1)
            random.shuffle(candidate_list)
            dataset[i] = {'prefs' : candidate_list, 'county' : random.randint(0, num_counties-1)}



    elif distribution == 'uniform-voters-non-uniform-candidates':
        candidate_list = range(1, num_candidates+1)

        if len(candidate_list) > 2 and len(candidate_list) < 10:
            #voters prefer a the first two candidates with igh probability and other candidates with low probability.  preference order given by shuffling list by first two.
            for i in range(num_voters):
                candidate_list = range(1, num_candidates+1)
                non_libertarian = random.random()
                if non_libertarian >= ((len(candidate_list) - 2) * 0.05):
                    top_choice = random.randint(1,2)
                    candidate_list.pop(top_choice-1)
                    random.shuffle(candidate_list)
                    dataset[i] = {'prefs' : [top_choice] + candidate_list, 'county' : random.randint(0, num_counties-1)}

                else:
                    top_choice = random.randint(3,num_candidates)
                    candidate_list.pop(top_choice-1)
                    random.shuffle(candidate_list)

                    dataset[i] = {'prefs' : [top_choice] + candidate_list, 'county' : random.randint(0, num_counties-1)}

        else:
            print ('Too many candidates for this option :(')
            quit()


    elif distribution == 'non-uniform-voters-uniform-candidates':
        #voters prefer a candidate with unfiorm probability.  preference order given by shuffling list.
        for i in range(num_voters):
            candidate_list = range(1, num_candidates+1)
            random.shuffle(candidate_list)
            county =  max(min(int(round(np.random.normal(num_counties / 2.0, num_counties / 6.0))) , num_counties - 1), 0)
            dataset[i] = {'prefs' : candidate_list, 'county' : county}


    elif distribution == 'non-uniform-voters-non-uniform-candidates':
        candidate_list = range(1, num_candidates+1)
        if len(candidate_list) > 2 and len(candidate_list) < 10:
            #voters prefer a the first two candidates with igh probability and other candidates with low probability.  preference order given by shuffling list by first two.
            for i in range(num_voters):
                county =  max(min(int(round(np.random.normal(num_counties / 2.0, num_counties / 6.0))) , num_counties - 1), 0)
                candidate_list = range(1, num_candidates+1)
                non_libertarian = random.random()
                if non_libertarian >= ((len(candidate_list) - 2) * 0.05):
                    top_choice = random.randint(1,2)
                    candidate_list.pop(top_choice-1)
                    random.shuffle(candidate_list)
                    dataset[i] = {'prefs' : [top_choice] + candidate_list, 'county' : county}

                else:
                    top_choice = random.randint(3,num_candidates)
                    candidate_list.pop(top_choice-1)
                    random.shuffle(candidate_list)

                    dataset[i] = {'prefs' : [top_choice] + candidate_list, 'county' : county}

        else:
            print ('Too many candidates for this option :(')
            quit()

    else:
        print ('I don\'t know what distribution you want :(')
        quit()

    return dataset

def writeoutput(dataset, filename):
    for voter_key, voter_vote in dataset.itervalues():
        pass
        #csv.write()

def summaryStats(dataset, num_candidates=4, num_counties=10):
    vote_counter = np.zeros(num_candidates)
    vote_locations = np.zeros(num_counties)
    for voter_key, voter_pref in dataset.iteritems():
        #print "Voter ID:  " + str(voter_key) + '\tTop preference:  ' + str(voter_pref['prefs'][0])
        try:
            vote_counter[voter_pref['prefs'][0] - 1] += 1
            vote_locations[voter_pref['county'] - 1] += 1

        except:
            print voter_pref['prefs'][0]
            quit()

    for i in range(num_candidates):
        print 'Candidate '+ str(i + 1) + ' votes:  ' + str(vote_counter[i])

    for j in range(num_counties):
        print 'County '+ str(j+1) + ' has ' + str(vote_locations[j]) +' people'


def main():
    dataset = datagen(5, 10, 10000, 'non-uniform-voters-non-uniform-candidates')

    summaryStats(dataset, 5, 10)


if __name__ == '__main__':
    main()
