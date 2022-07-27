"""
* write a program to find the position of a given number
  in a list of numbers arranged in decreasing order. [sorted already]
* We also need to minimize the number of times we access elements from the list.

list : cards
int : search  [find a certain value from a list called cards

 BINARY SEARCH
 - run-time is long for higher values
 - Big O is O(log N)
"""


def find_card(cards, search_card_value):
    low = 0
    high = len(cards) - 1
    """ can be written as 
        low, high = 0, len(cards) - 1
    """

    while low < high:
        mid = (low+high) // 2
        mid_card_value = cards[mid]

        if mid_card_value == search_card_value:
            return mid
        elif mid_card_value < search_card_value:
            high = mid - 1
        elif mid_card_value > search_card_value:
            high = mid + 1

    return f"Card {search_card_value} Does not exist in the deck"    # if the search_card value doesn't exist


print(find_card([9, 7, 5, 2, 1], 5))
