"""
Write a program to find the list of words that are longer than n from a given list of words.
"""

name_list = ['kiwi', 'banana', 'apple', 'orange', 'mango', 'pineapple']

def longer_word(name_list, n):
    new_list = []                    # new empty list created

    for i in name_list:              # for the elements in name_list
        if len(i) > n:               # if the length of count_item is greater than n
            new_list.append(i)       # add that count_item to the new list
    return new_list                  # return the new list


print(longer_word(name_list, 5))     # n=5 assigned



# -------------------------SPLIT method-----------------------------
def long_words(n, str):
    word_len = []
    txt = str.split(" ")

    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

print(long_words(3, "The quick brown fox jumps over the lazy dog"))
