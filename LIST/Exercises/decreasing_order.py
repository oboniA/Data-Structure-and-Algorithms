"""
write a program to find the position of a given number 
in a list of numbers arranged in decreasing order.
We also need to minimize the number of times we access elements from the list.

list : cards
int : search  [find a certain value from a list called cards
"""


def find_card(cards, search_card):
    card_position = 0

    print('Deck of cards: ', cards)
    print(f"find the position of card {search_card} from the deck")

    # use <, not <=; else it will return error, instead of while-return
    while card_position < len(cards):            # searching  is on, not reached the end
        if cards[card_position] == search_card:  # if the current index holds the card we are searching for
            return card_position                 # print that index where the card is present
        else:
            card_position += 1                   # keeps searching the card, from one address to the next address
    return f"Card {search_card} Does not exist in the deck"                     # if the search_card value doesn't exist


print(find_card([19, 17, 15, 11, 8, 4, 2], 20))
