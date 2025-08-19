"""
Practice Project: Arrays in Python 
This file contains multiple array problems for practicing:
- Access
- Insert
- Delete
- Search (linear, binary)
- Update

Each function has:
- Problem statement
- Example
- Constraints
"""

# -------------------------------
# Problem 1: Running Sum
# -------------------------------

def sum_function(nums):
    """
    Given a one-dimensional array of integers, return an array
    where result[i] = sum(nums[0] ... nums[i]).

    Example:
    Input: [2, 3, 5, 1, 6]
    Output: [2, 5, 10, 11, 17]

    Constraints:
    - 1 <= len(nums) <= 1000   -> small enough for O(n) loop
    - -10^6 <= nums[i] <= 10^6
    """
    # TODO: implement using prefix sums
    result = []
    temp = 0
    for num in nums:
        temp += num
        result.append(temp)
    return result

# Practice Variations:
def sum_inplace(nums):
    """Modify nums in-place instead of creating new array."""
    for i in range(1, len(nums)): 
        nums[i] += nums[i-1]
    return nums

def insert(nums, x):
    """After computing running sum, insert value x at the end."""
    nums.append(x)
    return nums

def insert_at(nums, x, at):
    """
    1. Insert value x at index at.
    2. Return the updated array.
    """
    nums.insert(at, x)
    
    return nums

# -------------------------------
# Problem 2: Contains Duplicate
# -------------------------------

def contains_duplicate(nums):
    """
    Return True if any number appears at least twice, else False.

    Example:
    Input: [1, 2, 3, 1] -> True
    Input: [1, 2, 3, 4] -> False

    Constraints:
    - 1 <= len(nums) <= 10^5  -> too large for O(n^2)
      -> use HashSet (O(n)) or sorting (O(n log n))
    """
    # TODO: implement using set
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False

# Practice Variations:
def find_first_duplicate(nums):
    """Return the index of first duplicate value found, else None."""
    s = set()
    for i, num in enumerate(nums):
        if num in s:
            return nums[i]
        s.add(num)
    return False

def count_duplicates(nums):
    """Return what elements appear more than once."""
    freq = {}
    duplicates = []

    # Count frequency of each number
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # Collect numbers that appear more than once
    for value, times in freq.items():
        if value > 1: # 2 or more reapeated
            duplicates.append(times)

    return duplicates
# -------------------------------
# Problem 3: Difference Array
# -------------------------------

def difference_array(nums):
    """
    For each index i, compute:
    difference[i] = |sum(left of i) - sum(right of i)|

    Example:
    Input: [2, 5, 1, 6, 1]
    Output: [13, 6, 0, 7, 14]

    Constraints:
    - 1 <= len(nums) <= 1000  -> O(n^2) possible, but O(n) with prefix sums better
    """
    # TODO: use prefix sums (efficient)
    total = sum(nums) # total sum of array
    left_sum = 0;
    result = [] 

    for num in nums:
        right_sum = total - left_sum - num
        result.append(abs(left_sum - right_sum))
        left_sum += num
    return result

# Practice Variations:
def difference_array_bruteforce(nums):
    """with nested loops (O(n^2)) for learning purposes."""
    n = len(nums)
    res = []

    for i in range(n):
        # sum left part (0 ... i-1)
        left_sum = 0
        for j in range(i):
            left_sum += nums[j]

        # sum right part (i+1 to n-1)
        right_sum = 0
        for j in range(i+1, n):
            right_sum += nums[j]

        # absolute difference
        res.append(abs(left_sum - right_sum))

    return res

def difference_array_update(nums, index, new_value):
    """Update nums[index] = new_value and recompute difference array."""
    pass

# -------------------------------
# Problem 4: Highest Altitude
# -------------------------------

def highest_altitude(gain):
    """
    Given net gain between points, return highest altitude reached.

    Example:
    Input: [-5, 1, 5, 0, -7]
    Output: 1

    Constraints:
    - 1 <= len(gain) <= 100   -> O(n) fine
    - -100 <= gain[i] <= 100
    """
    # TODO: track cumulative sum and max
    pass


# Practice Variations:
def altitude_path(gain):
    """Return the full altitude path as a list, not just the max."""
    pass

def count_positive_altitudes(gain):
    """Return how many times the altitude went above 0."""
    pass


# -------------------------------
# HOW TO USE
# -------------------------------
if __name__ == "__main__":
    # try filling in your solutions and testing here
    nums = [2, 3, 5, 1, 6]
    print("Running sum:", sum_function(nums))  # expected sum
    nums = [0]
    print("Running sum:", sum_function(nums))  # expected sum
    nums = [-10, -9, 0, 0, 0]
    print("Running sum:", sum_function(nums))  # expected sum
    nums = [-30]
    print("Running sum:", sum_function(nums))  # expected sum

    nums = [2, 3, 5, 1, 6]
    print("Sum in place:", sum_inplace(nums)) # return modified array rather than a copy
    print(insert(nums, 20)) # Insert 20 at the end

    print(insert_at([2,3,5,1,6], 99, 4)) # Insert 12 in index 3


    nums = [1, 2, 3, 1]
    print("Contains duplicate:", contains_duplicate(nums))  # expected True
    nums = [1, 2, 3, 4]
    print("Contains duplicate:", contains_duplicate(nums))  # expected False
    nums = [1, 2, 3, 3, 2]
    print("Find first duplicate:", find_first_duplicate(nums))
    print("Count duplicates:", count_duplicates(nums))


    nums = [2, 5, 1, 6, 1]
    print("Difference array:", difference_array(nums))  # expected [13, 6, 0, 7, 14]
    print("Difference array brute-force:", difference_array_bruteforce(nums))  # expected [13, 6, 0, 7, 14]


    gain = [-5, 1, 5, 0, -7]
    print("Highest altitude:", highest_altitude(gain))  # expected 1
