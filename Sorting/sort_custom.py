from typing import List

def get_word_length(word: str) -> int:
    return len(word)

def get_absolute_num(num: int) -> int:
    return abs(num)

def sort_words(words: List[str]) -> List[str]:
    #sorted based on their length, in descending order
    words.sort(key=get_word_length, reverse=True) 
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    #return numbers sorted based on their absolute, value in asending order
    numbers.sort(key=get_absolute_num)
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
