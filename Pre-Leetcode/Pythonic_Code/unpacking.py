from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    #takes 3 integers and returns the sume of the integ takes 3 intgers and returns the sum of que
    #takes 3 integers and returns the sum of the integers
    x1, x2, x3 = triplet
    return x1 + x2 + x3

def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    #takes a lis of 3 integers width, height, depth, returns the volume of it
    x1, x2, x3 = box_dimensions
    return x1 * x2 * x3

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
