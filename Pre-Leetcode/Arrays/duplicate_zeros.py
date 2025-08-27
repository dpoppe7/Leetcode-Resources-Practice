from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0) # counts number of zero in arr
        n = len(arr)
        
        for i in range(n-1, -1, -1):
            # This print statement should now execute
            print(f"Current index: {i}, Zeroes count: {zeroes}, Array length: {n}")
            
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
                # This print statement will execute if the condition is met
                print(f"Swapping from {i} to {i + zeroes}")
            if arr[i] == 0:
                zeros -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


if __name__ == "__main__":
    solution = Solution()  # Create an instance of the class
    
    arr = [1,0,2,3,0,4,5,0]
    
    solution.duplicateZeros(arr) # Call the method on the instance
    
    print("Final array:", arr)