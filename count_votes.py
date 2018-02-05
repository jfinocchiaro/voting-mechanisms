import random
import random_data_generate
import numpy as np


num_candidates = 4
def popular_vote(dataset):
    top_prefs = []
    pref_arr = np.zeros(num_candidates)
    for voter_key, voter_pref in dataset.iteritems():
        top_prefs.append(voter_pref['prefs'][0])
        pref_arr[voter_pref['prefs'][0] - 1] += 1

    winner = max(set(top_prefs), key=top_prefs.count)
    return winner

def electoral_college(dataset, num_candidates, num_counties):
    county_votes = {}
    for i in range(0, num_counties):
        county_votes[i] = []

    electoral_votes = np.zeros(num_candidates)

    for voter_key, voter_pref in dataset.iteritems():
        county_votes[voter_pref['county']].append(voter_pref['prefs'][0])

    for county, votes in county_votes.iteritems():

        if len(votes) > 0 :
            county_winner = max(set(votes), key=votes.count)
            electoral_votes[county_winner - 1] += len(votes)



    electoral_votes = list(electoral_votes)
    winner = max(electoral_votes)

    return electoral_votes.index(winner) + 1


def quadratic_vote(dataset):
    candidate_votes = np.zeros(num_candidates)
    for voter_key, voter_pref in dataset.iteritems():
        prefs = voter_pref['prefs']
        for i in range(len(prefs)):
            candidate_votes[prefs[i] - 1] += (num_candidates - i) ** 2
    candidate_votes = list(candidate_votes)
    winner = max(candidate_votes)
    return candidate_votes.index(winner) + 1


def point_system(dataset, num_candidates):
    candidate_votes = np.zeros(num_candidates)
    for voter_key, voter_pref in dataset.iteritems():
        prefs = voter_pref['prefs']
        for i in range(len(prefs)):
            candidate_votes[prefs[i] - 1] += num_candidates - i
    candidate_votes = list(candidate_votes)
    winner = max(candidate_votes)
    return candidate_votes.index(winner) + 1


def main():
    num_candidates = 4
    num_counties = 20
    num_voters = 10000
    vote_distribution = 'uniform-voters-uniform-candidates'
    #random_data_generate has parameters: num_candidates, num_counties, num_voters
    dataset= random_data_generate.datagen(num_candidates, num_counties, num_voters, vote_distribution)

    print 'Popular vote winner:  ' + str(popular_vote(dataset))
    print 'Electoral college winner:  ' + str(electoral_college(dataset, num_candidates, num_counties))
    print 'Point System winner:  ' + str(point_system(dataset, num_candidates))
    print 'Quadratic vote winner:  ' + str(quadratic_vote(dataset))
    print '-----------------------------'

    random_data_generate.summaryStats(dataset, num_candidates, num_counties)


if __name__ == '__main__':
    main()
