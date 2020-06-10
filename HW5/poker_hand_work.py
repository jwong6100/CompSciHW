#Author - Jonathan Wong, jfw5328@psu.edu

if __name__ == '__main__':
    from poker_hand_import import shuffle_deck,summarize,test, \
        card_name,short_name,print_hand,print_short_hand

# A couple lists describing the cards of a hand
# The ranks are listed so the highest card will be easy to identify

suits = ['Clubs','Diamonds','Hearts','Spades']

ranks = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight',
         'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']

types = ['Straight Flush','Four of a Kind','Full House','Flush',
         'Straight','Three of a Kind','Two Pair','Pair','Nothing']


# The Student Work for this assignment is Below This Line

# Here are some functions to help categorize a hand

def count_ranks(hand):
    '''Returns the number of twos, threes, etc. in a hand'''
    counts = [0] * 13                # initialize counts for all 13 ranks
    
    #going through cards in hand
    for card in hand:
        counts[card[0]] += 1
        return counts
 
    return counts

def longest_suit(hand):
    '''Returns the longest subset of a hand in the same suit
    Five cards in one suit counts as a Flush'''
    suit_sets = [[],[],[],[]]      # four empty lists

    #going through cards in hand and adding them to list array.
    for card in hand:
        if card[1] == 1:
            suit_sets[0].append(card)
        elif card[1] == 2:
            suit_sets[1].append(card)
        elif card[1] == 3:
            suit_sets[2].append(card)
        elif card[1] == 4:
            suit_sets[3].append(card)
            
    #determining longest suit        
    while (len(suit_sets) > 1):
        if len(suit_sets[0]) >= len(suit_sets[1]):
            del suit_sets[1]
        else:
            del suit_sets[0]

    answer = suit_sets[0]
 
    return answer

def contains_straight(counts):
    '''identifies whether the hand is a straight
    if so, returns the rank of the high card in the straight,
    otherwise simply returns False'''

    #try, except blocks
    try:
        index = counts.index(1)
    except:
        return False
    #see if cards are straight
    try:
        if counts[index] == counts[index + 1] == counts[index + 2] == counts[index + 3] == counts[index + 4]:
            return True
        elif index == 0:
            if counts[index] == counts[index - 1] == counts[index - 2] == counts[index - 3] == counts[index - 4]:
                return True
        else:
            return False
    except:
        return False
            
    return False

def evaluate_hand(hand):
    '''Categorizes a hand of cards
    Returns a tuple, containing these two features:
        The kind of hand (an element listed in _types_ above
        The numeric rank of card to further describe the hand, which may be
            a tuple representing two ranks for Full House or Two Pair
            a rank that appears four times in Four of a Kind
            a rank that appears three times in Three of a Kind
            a rank of a Pair (when there is only one pair)
            a rank at the top of a Straight, Flush, or Other'''

    #full house
    for i in count_ranks(hand):
        if count_ranks(hand)[i] == 3:
            for j in count_ranks(hand):
                if count_ranks(hand)[j] == 2:
                    return types[2], (i,j)

    #two pair    
    for i in range(len(count_ranks(hand))):
        if count_ranks(hand)[i] == 2:
            for j in range(i + 1, len(count_ranks(hand))):
                if count_ranks(hand)[j] == 2:
                    return types[6], ranks[i]
                else:
                    #one pair
                    return types[7], i 

    #four of a kind
    for card in count_ranks(hand):
        if count_ranks(hand)[card] == 4:
            return types[1], card

    #three of a kind
    for i in count_ranks(hand):
        if count_ranks(hand)[i] == 3:
            return types[5], i
    
    #straight
    if contains_straight(hand):
        if len(longest_suit(hand)) == 4:
            return types[0], count_ranks(hand).index(1)
                
    #flush
    if len(longest_suit(hand)) == 5:
        return types[3], count_ranks(hand).index(1)

    #flush #2
    if contains_straight(hand):
        return types[4], count_ranks(hand).index(1)

    #other
    return types[8], count_ranks(hand).index(1)



def better_hand(hand1,hand2):
    '''Determines which of two hands is better than the other
    Returns None if they are of equal value'''
    
    kind1,rank1 = evaluate_hand(hand1)
    kind2,rank2 = evaluate_hand(hand2)

    #comparing hands
    if types.index(kind1) < types.index(kind2):
        return hand1
    elif types.index(kind1) > types.index(kind2):
        return hand2
    else:
        if rank1 > rank2:
            return hand2
        else:
            return hand1

    


if __name__ == '__main__':
    for i in range(1):
        test()

