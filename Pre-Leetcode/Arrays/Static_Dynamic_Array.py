# Task: "Dynamic Movie Ratings Tracker" 🎬
# building a tool to track movie ratings for a streaming service.

# Your program should:
# 1. Start with a static array of fixed size n (the initial capacity).
# 2. Allow adding ratings one at a time.
# 3. If the array is full, resize it to double the capacity (dynamic array behavior).
# 4. Implement functions to:
#   Add a rating
#   Remove a rating by index
#   Find the highest rating
#   Find the average rating
#   Search if a rating exists
#   Sort ratings (ascending and descending)
# 5. Return the ratings as a list at any point.


from typing import List

class MovieRatings:
    # Constructor: Special method that sets up the Object when it's create
    # In phyton always __init__
    def __init__(self, capacity=5):
        # self is the reference to the object itself 
        # (so we store data on it)
        
        # These are Instance Properties, in Python also called Attributes 
        # Attributes live in self
        self.capacity = capacity 
        self.size = 0
        self.data = [None] * self.capacity # Empty array, [None, None, None, None, None]
        
    # Destructor: Method to clean up when object is about to be destroyed.
    # In Python → __del__.
    # Rarely needed because Python’s garbage collector handles most cleanup.
    
    # There's also __str__ → string representation
       
    # Methods: functions that belong to a class, and operate on its data 
    
    # Re4size array
    def _resize(self):
        # double the array size and copy contents to new list
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        
        # Copy elements from old array to new one
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self.capacity = new_capacity
        
    
    # Add a rating
    def add_rating(self, rating):
        if self.size == self.capacity:
            self._resize()  # expand the array when full
        self.data[self.size] = rating
        self.size += 1

    # remove a rating
    def remove_rating(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
    
        # Shift left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        # Clear the last slot
        self.data[self.size - 1] = None
        
        # Reduce size
        self.size -= 1
        
    # find highest rating
    def find_highest(self):
        # TODO: Loop through the array (only size elements) to find max
        if self.size == 0:
            raise ValueError("No ratings to evaluate")
        max = self.data[0]
        for i in range(1, self.size):
            if self.data[i] > max:
                max = self.data[i]
        return max
        
    # find the average rating
    def find_average(self):
        if self.size == 0:
            raise ValueError("Empty List")
            
        total = 0
        for i in range(self.size):
            total += self.data[i]
        return total / self.size

    # search if a rting exists
    def search_rating(self, rating):
        for i in range(self.size):
            if self.data[i] == rating:
                return True
        return False
        
    # sort rating ascending and descending
    def sort_ratings(self, desc = False):
        sorted_chunk = sorted(self.data[:self.size], reverse = desc)
        self.data[:self.size] = sorted_chunk
        
        # without creating a new list 
        chunk = self.data[:self.size]
        chunk.sort(reverse=desc)        # sorts the temporary list
        self.data[:self.size] = chunk
        
    # get ratings: returns only the filled part of the array
    def get_ratings(self):
        return self.data[:self.size]

# TESTING IMPLEMENTATION
# -------------------------
if __name__ == "__main__":
    
    # Object/Instance of class MovieRatings
    tracker = MovieRatings(capacity=5)

# Initial capacity = 5
print(tracker.data)
tracker.add_rating(8)
tracker.add_rating(5)
tracker.add_rating(10)
tracker.add_rating(7)
tracker.add_rating(9)
print(tracker.data)
tracker.remove_rating(0)
# Static array is now full

print(tracker.find_highest())  # 10
print(tracker.find_average())  # 7.0
print(tracker.search_rating(5))  # True
tracker.sort_ratings(desc=True)
print(tracker.data)
print(tracker.get_ratings())  # [9, 8, 7, 6, 5]