from typing import List, Tuple, Union

def analyze_sequence(seq: Union[List[int], Tuple[int, ...]]) -> Tuple[int, int, int]:
    #Returns a tuple with: the first element, the sum of all the middle elements, the last element.
    first, *middle, last = seq
    middle_sum = sum(middle)
    return first, middle_sum, last

print(analyze_sequence([10, 20, 30, 40, 50])) # Output: (10, 90, 50) because 20+30+40 = 90
print(analyze_sequence((1, 2, 3))) # Output: (1, 2, 3) because middle is just [2], sum=2