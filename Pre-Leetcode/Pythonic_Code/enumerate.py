from typing import List, Tuple

def filter_and_tag(words: List[str]) -> List[Tuple[int, str]]:
    #Returns a new list of tuples (index, word) only if:
    #   The index is odd.
    #   The word’s length is greater than 5.
    #Return the words in reverse order ("banana" → "ananab")
    new_list = []
    for index, word in enumerate(words):
        if index % 2 != 0 and len(word) > 5 :
            new_list.append((index, ''.join(reversed(word))))      
    return new_list

def filter_slicing(words: List[str]) -> List[Tuple[int, str]]:
    #Same but using python slicing
    new_list = []
    for index, word in enumerate(words):
        if index % 2 != 0 and len(word) > 5 :
            new_list.append((index, word[::-1]))
    return new_list

print(filter_and_tag(["apple", "banana", "cherry", "date", "elderberry", "figure"]))
print(filter_slicing(["apple", "banana", "cherry", "date", "elderberry", "figure"]))
# Expected output: [(1, 'ananab'), (4, 'yrrebredle')]
