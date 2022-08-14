"""
Find the list of words
that are longer than n
from a given list of words
"""


list1 = ['bubble', 'exist', 'long', 'tea', 'go']
new_list = []
n = int(input("value of n: "))

for element in list1:
    if len(element) > n:
        new_list.append(element)
print(new_list)








'''
txt = str.split("the name of that person was xyz and they did ballet")
word_list = []

for e in txt:
    if len(e) > 3:
        word_list.append(e)
print(word_list)
'''




'''
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

'''