from heapq import heappop, heappush
from typing import List


class Solution:
    # Go over once left to right and right to left
    # Time O(n) as we go over ratings multiple times
    # Space O(n) we store just one extra array this time
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        candies = [1] * len(ratings)
        # Go left to right and add candies as need be
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        answer = candies[-1]
        # Go right to left and add candies as need be
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

            answer += candies[i]

        return answer
    
    # Have left to right array and right to left array then take max
    # Time O(n) as we go over ratings multiple times
    # Space O(n) to store left to right array and right to left array
    def candy_two_arrays(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Populate how many required if going left to right
        left_to_right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_to_right[i] = left_to_right[i-1] + 1

        # Populate how many required if going right to left
        right_to_left = [1] * n
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right_to_left[i] = right_to_left[i+1] + 1

        # Find answer by finding max of the two
        answer = 0
        for i in range(n):
            answer += max(left_to_right[i], right_to_left[i])

        return answer
    
    # Min priority queue of ratings. 
    # Each time we pop make sure more than neighbors if needed
    # Time O(nlogn) to make priority queue
    # Space O(n) to store candies array
    def candy_priority_queue(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Array for how many candies each child gets
        candies = [1] * n

        # Sort index by min rating
        ratings_min_heap = []
        for index, rating in enumerate(ratings):
            heappush(ratings_min_heap, (rating, index))

        total = n
        # Every time we pop from heap if index is higher than neighbor
        # Then give that +1 level of candies
        while ratings_min_heap:
            rating, index = heappop(ratings_min_heap)

            to_add = 0
            # Check if neighbor to left is lower rating
            if index - 1 >= 0 and ratings[index] > ratings[index-1]:
                to_add = candies[index-1]

            # Check if neighbor to right is lower rating
            if index + 1 < n and ratings[index] > ratings[index+1] and candies[index+1] > to_add:
                to_add = candies[index+1]

            total += to_add
            candies[index] += to_add

        return total
    
test_cases = [
    [5, [1,0,2]],
    [4, [1,2,2]]
]
solution = Solution()
for expected, ratings in test_cases:
    actual = solution.candy(ratings)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: ratings: {ratings}")

print("Ran all tests")