from typing import List


class Solution:
    # Time O(n)
    # Space O(1)
    def minSwaps(self, data: List[int]) -> int:
        # Count how many ones there are, then create a window of that size
        # Whatever window has the smallest number of 0's in it that wins
        min_zeros = float("inf")
        ones_count = 0
        n = len(data)

        # Count how many ones
        for num in data:
            if num == 1:
                ones_count += 1

        # Make sure there are at least 2 1's so a swap is possible
        if ones_count <= 1:
            return 0
        
        # Create the initial window and slide it until the end and return the min
        right = zeroes_count = 0
        while right < ones_count:
            if data[right] == 0:
                zeroes_count += 1
            right += 1

        min_zeros = min(min_zeros, zeroes_count)

        for i in range(n - ones_count):
            if data[i] == 0:
                zeroes_count -= 1
            if data[right] == 0:
                zeroes_count += 1

            right += 1
            min_zeros = min(min_zeros, zeroes_count)

        return min_zeros
    
test_cases = [
    [1, [1,0,1,0,1]],
    [0, [[0,0,0,1,0]]],
    [3, [1,0,1,0,1,0,0,1,1,0,1]],
    [19, [0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]]
]
solution = Solution()
for expected, data in test_cases:
    actual = solution.minSwaps(data)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: data: {data}")

print("Ran all tests")