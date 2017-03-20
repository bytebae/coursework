# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.
#
# The itertools library may be helpful. Feel free to 
# define multiple functions if it helps you solve the
# problem. 
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."

    # Your code here

    # get all combinations first
    # then expand combinations where jokers are present
    # then choose highest rank from all combinations
    
    "Take (5-7) card hand with jokers and return a 5-card hand"
    if '?R' not in hand and '?B' not in hand:
        print "asserted value due to no wildcards: {}".format(best_hand(hand))
        return best_hand(hand)
    joker_combination_list = recursively_replace_jokers(hand, [[]])
    result = []
    for l in joker_combination_list:
        result.append(best_hand(l))
    maxim, max_hand = -1, []
    for m in result:
        if hand_rank(m) > maxim:
            maxim, max_hand = hand_rank(m), m
    print "asserted value: %s" % str((max_hand))
    print "-------------------------"
    return max_hand
    
def recursively_replace_jokers(hand, return_hands=[[]]):
    if len(hand) == 0:
        return return_hands
    if hand[0] != '?R' and hand[0] != '?B':
        map((lambda x: x.append(hand[0])), return_hands)
        return recursively_replace_jokers(hand[1:], return_hands)
    else:
        return_hands = [card for card in return_hands for i in range(26)]
        return_hands = map((lambda (x,y): x+[y]), zip(return_hands, list_of_replacements(hand[0][1])*(len(return_hands)/26)))
        return_hands = map(list, map(set, return_hands))
        return recursively_replace_jokers(hand[1:], return_hands)
    
def list_of_replacements(color):
    if color.upper() == 'R':
        list_of_all_poss_red_cards = [r+s for r in map(str, range(2,10)+['A', 'K', 'Q', 'J', 'T']) for s in ['D', 'H']]
        return list_of_all_poss_red_cards
    else:
        list_of_all_poss_black_cards = [r+s for r in map(str, range(2, 10)+['A', 'K', 'Q', 'J', 'T']) for s in ['S', 'C']]
        return list_of_all_poss_black_cards

def best_hand(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("TD TC 5H ?R 5C ?B 7C".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])

    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your b['6C', '5B', '3C', '7B', '8B', '10B', '?R', '?B']est_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
    
print test_best_wild_hand()
