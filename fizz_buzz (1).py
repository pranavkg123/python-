# -*- coding: utf-8 -*-
"""fizz_buzz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BFoRRXUSoDfXUHv3Jzns55SFlBEgdJ-N
"""

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]