# Poker Hand Evaluator
# Given a set of cards representing a poker hand,
# identifies the nature of that hand.

import random
from poker_hand_work import evaluate_hand,better_hand

# A couple lists describing the cards of a hand
# The ranks are listed so the highest card will be easy to identify

suits = ['Clubs','Diamonds','Hearts','Spades']

ranks = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight',
         'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']

types = ['Straight Flush','Four of a Kind','Full House','Flush',
         'Straight','Three of a Kind','Two Pair','Pair','Nothing']

# Some descriptive items

def card_name(card):
    '''Returns the name of a card, given its coded rank and suit'''
    return ranks[card[0]] + ' of ' + suits[card[1]]

def print_hand(hand):
    '''Prints the long names of the cards in a hand'''
    for card in sorted(hand):
        print(card_name(card),end='  ')
    print()

def short_name(card):
    '''Identifies a card by a very brief name'''
    return 'AKQJT98765432'[card[0]] + 'CDHS'[card[1]]

def print_short_hand(hand):
    '''Prints the short names of the cards in a hand'''
    for card in sorted(hand):
        print(short_name(card),end=' ')

def summarize(hand):
    if hand is None:
        print('No winning hand')
        return
    hand_type,rank = evaluate_hand(sorted(hand))
    print_short_hand(hand)
    print('--',hand_type,end=' ')
    if hand_type == 'Full House':
        print(f'{ranks[rank[0]]}s over {ranks[rank[1]]}s')
    elif hand_type == 'Two Pair':
        print(f'{ranks[rank[0]]}s and {ranks[rank[1]]}s')
    elif hand_type in ['Four of a Kind','Three of a Kind','Pair']:
        print(ranks[rank])
    else:
        print(f'{ranks[rank]} high')

# Randomly generate hands of rare types

def random_flush():
    '''Creates a flush, that may or may not be a straight'''
    suit = random.randint(0,3)
    hand = []
    for rank in random.sample(range(13),5):
        hand.append( (rank,suit) )
    return sorted(hand)

def random_straight():
    '''Creates a straight, that may or may not be a flush'''
    suit = random.randint(0,3)
    other = random.randint(0,3)
    first = random.randint(-1,8)
    if first == -1:     # Create Ace-low straight
        first = 8
        hand = [ (0,other) ]
    else:
        hand = [ (first,other) ]
    for i in range(1,5):
        hand.append( (first+i,suit) )
    return sorted(hand)

def shuffle_deck():
    '''Returns a complete deck of cards, shuffled; each card is a tuple'''
    deck = []
    for suit in range(4):
        for rank in range(13):
            deck.append( (rank, suit) )
    random.shuffle(deck)
    return deck

# Here a few tests to start with:
def test():
    deck = shuffle_deck()
    for j in range(0,40,10):
        summarize(deck[j:j+5])
        summarize(deck[j+5:j+10])
        print_hand(better_hand(sorted(deck[j:j+5]),sorted(deck[j+5:j+10])))
        
    hand1 = random_straight()
    hand2 = random_straight()
    summarize(hand1)
    summarize(hand2)
    print_hand(better_hand(hand1,hand2))
    
    hand1 = random_flush()
    hand2 = random_flush()
    summarize(hand1)
    summarize(hand2)
    print_hand(better_hand(hand1,hand2))

