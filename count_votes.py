import random
import random_data_generate
import numpy as np

def popular_vote(dataset):
    top_prefs = []
    for voter_key, voter_pref in dataset.iteritems():
        top_prefs.append(voter_pref['prefs'][0])
    winner = max(set(top_prefs), key=top_prefs.count)
    return winner

def electoral_college(dataset, num_candidates, num_counties):
    county_votes = {}
    for i in range(1, num_counties+1):
        county_votes[i] = []

    electoral_votes = np.zeros(num_candidates)

    for voter_key, voter_pref in dataset.iteritems():
        county_votes[voter_pref['county']].append(voter_pref['prefs'][0])


    for county, votes in county_votes.iteritems():
        county_winner = max(set(votes), key=votes.count)
        electoral_votes[county_winner - 1] += len(votes)

    electoral_votes = list(electoral_votes)    
    winner = max(set(electoral_votes), key=electoral_votes.count)
    return electoral_votes.index(winner) + 1


def quadratic_vote(dataset):
    pass

def point_system(dataset):
    pass


def main():
    num_candidates = 4
    num_counties = 20
    num_voters = 1000
    vote_distribution = 'uniform-voters-uniform-candidates'
    #random_data_generate has parameters: num_candidates, num_counties, num_voters
    dataset= random_data_generate.datagen(num_candidates, num_counties, num_voters, vote_distribution)
    print 'Popular vote winner:  ' + str(popular_vote(dataset))
    print 'Electoral college winner:  ' + str(electoral_college(dataset, num_candidates, num_counties))
    quit()
    print 'Quadratic vote winner:  ' + str(quadratic_vote(dataset))
    print 'Point System winner:  ' + str(point_system(dataset))



if __name__ == '__main__':
    main()
