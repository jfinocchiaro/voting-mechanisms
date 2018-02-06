import random_data_generate
import count_votes
import numpy as np
import random


def multi_trials(num_trials=500, num_candidates=4, num_counties=20, num_voters=1000, distribution='uniform-voters-uniform-candidates'):
    odd_votes_out = np.zeros(4)
    num_winners_tally = np.zeros(4)

    for i in range(num_trials):
        dataset = random_data_generate.datagen(num_candidates, num_counties, num_voters, distribution)
        pop_vote = count_votes.popular_vote(dataset, num_candidates)
        ec_vote = count_votes.electoral_college(dataset, num_candidates, num_counties)
        point_vote = count_votes.point_system(dataset, num_candidates)
        quad_vote = count_votes.quadratic_vote(dataset, num_candidates)
        num_winners_tally[len(set([pop_vote, ec_vote, point_vote, quad_vote])) - 1] += 1

        if len(set([pop_vote, ec_vote, point_vote, quad_vote])) == 2:
            if pop_vote != ec_vote and pop_vote != point_vote and pop_vote != quad_vote:
                odd_votes_out[0] += 1
            elif ec_vote != pop_vote and  ec_vote != point_vote and  ec_vote != quad_vote:
                odd_votes_out[1] += 1
            elif point_vote != pop_vote and point_vote != ec_vote and point_vote != quad_vote:
                odd_votes_out[2] += 1
            elif quad_vote != pop_vote and quad_vote != ec_vote and quad_vote != point_vote:
                odd_votes_out[3] += 1


    agreement_count = num_winners_tally[0]
    print 'Total agreement ' + str(agreement_count) + ' out of ' + str(num_trials) +' times.  That\'s ' + str(float(agreement_count) / num_trials * 100) + '% of the time with ' + distribution + ' distribution and ' + str(num_candidates) + ' candidates'
    print 'There were ' + str(num_winners_tally[0]) + ' instances of total agreement, ' + str(num_winners_tally[1]) + ' instances with two winners, ' + str(num_winners_tally[2]) + ' instances with three winners, and ' + str(num_winners_tally[3]) + ' instances with four unique winners.'
    print 'Odd votes out:  ' + str(odd_votes_out)

def main():
    multi_trials(distribution='non-uniform-voters-uniform-candidates')
if __name__ == '__main__':
    main()
