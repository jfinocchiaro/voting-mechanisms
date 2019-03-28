import random
import numpy as np
import csv

def gen_dataset(filename):
    voters = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            voter = {}
            time = row.pop(0)
            ordered_pref = row[0:5]
            del row[0:5]
            voter['order'] = ordered_pref
            approved = [x.split(';') for x in row][0]
            voter['approved'] = approved
            voters.append(voter)

    return voters

def majority_vote(dataset, num_candidates=5):
    #don't think we need this, but keeping it in now just in case.  This is each person's top choice as a list
    top_prefs = []
    #counts the number of votes each candidate receives
    vote_counter = np.zeros(num_candidates)

    for voter in dataset:
        order = voter['order']
        top_choice = order.index('Rank 1 (most preferred)')
        top_prefs.append(top_choice)
        vote_counter[top_choice] += 1

    vote_weight = max(vote_counter)
    winners, = np.where(vote_counter == vote_weight)

    return winners, vote_counter


def polynomial_vote(dataset, num_candidates = 5, exponent=2):
    #counts the number of votes each candidate receives
    vote_counter = np.zeros(num_candidates)

    for voter in dataset:
        order = voter['order']

        for idx, rank in enumerate(order):
            if rank == 'Rank 1 (most preferred)':
                vote_counter[idx] += ((num_candidates - 1) ** exponent)
            elif rank == 'Rank 2':
                vote_counter[idx] += ((num_candidates - 2) ** exponent)
            elif rank == 'Rank 3':
                vote_counter[idx] += ((num_candidates - 3) ** exponent)
            elif rank == 'Rank 4':
                vote_counter[idx] += ((num_candidates - 4) ** exponent)
            elif rank == 'Rank 5 (Least preferred)':
                vote_counter[idx] += 0
            else:
                print "Invalid ranking"
                quit()

    vote_weight = max(vote_counter)
    winners, = np.where(vote_counter == vote_weight)

    return winners, vote_counter


def borda(dataset, num_candidates):
    return polynomial_vote(dataset, num_candidates, exponent=1)


def irv(dataset, num_candidates):
    options = ['Bring back Mordechai', 'Clear the horde', 'Dimmadome', 'Space captains', 'Take the money']
    remaining = np.ones(num_candidates)
    remaining_candidates = range(num_candidates)
    voter_lists = []
    #for each voter, create ordered list of outcomes
    for voter in dataset:
        ranks = voter['order']
        voter_lists.append([ranks.index('Rank 1 (most preferred)'), ranks.index('Rank 2'), ranks.index('Rank 3'), ranks.index('Rank 4'), ranks.index('Rank 5 (Least preferred)') ])

    while(len(remaining_candidates) > 1):
        top_votes = [0] * num_candidates
        for voter in voter_lists:
                top_votes[voter[0]] += 1
        tot_votes = [opt for i, opt in enumerate(top_votes) if remaining[i] == 1]
        least_votes = min(tot_votes)

        loser_idx_sm = tot_votes.index(least_votes)
        removed = -1

        for i in range(num_candidates):
            if (remaining[i] == 1) and (top_votes[i] == least_votes):
                remaining[i] = 0
                removed = i
                break
            else:
                pass

        del remaining_candidates[loser_idx_sm]

        for voter in voter_lists:
            idx = voter.index(removed)
            del voter[idx]

    winners, = np.where(remaining == 1)

    return winners

def veto(dataset, num_candidates):
    options = {'Bring back Mordechai': 0, 'Clear the horde':0, 'Dimmadome':0, 'Space captains':0, 'Take the money':0}
    for voter in dataset:
        approved = voter['approved']

        for option in approved:
            if option in options.keys():
                options[option] += 1

    max_approvals = max(options.values())

    winners = [key for key in options.keys() if (options[key] == max_approvals)]

    return [winners, options]

def main(filename):
    num_candidates = 5
    dataset = gen_dataset(filename)
    options_by_name = ['Bring back Mordechai','Clear the horde','Dimmadome','Space captains','Take the money']

    print '---------------------------------------------------------'
    [majority_winner, score_majority] = majority_vote(dataset)
    print 'Majority vote winner(s):\t' + str([options_by_name[winner] for winner in majority_winner])

    [polynomial_winner, score_poly] = polynomial_vote(dataset, num_candidates)
    print 'Polynomial vote winner(s):\t' + str([options_by_name[winner] for winner in polynomial_winner])

    [borda_winner, score_borda] = borda(dataset, num_candidates)
    print 'Borda winner(s):\t\t' + str([options_by_name[winner] for winner in borda_winner])

    [veto_winners, approvals] = veto(dataset, num_candidates)
    print 'Veto winner(s):\t\t\t' + str(veto_winners)

    irv_winners = irv(dataset, num_candidates)
    print 'Instant runoff winner(s):\t' + str([options_by_name[winner] for winner in irv_winners])
    print '---------------------------------------------------------'



if __name__ == '__main__':
    filename = 'LuckBladeWish.csv'
    main(filename)
