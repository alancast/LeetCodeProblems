from typing import List


class Solution:
    # Sort nums then go over all nums
    # For every num see if it can be appended to the already created subsets
    # Find longest subset and then work backwards
    # Time O(n^2) as for each index go through every index before it
    # Space O(n) as we keep dp array of size nums
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        # longest subset ending at this num
        longest_streak_ending_here = [0] * n
        
        # Go over every num and see if it can continue a subset
        for i, num in enumerate(nums):
            max_len = 1
            # Go over all previous subsets and see if this can append and find distance
            for j in range(i):
                if num % nums[j] == 0 and longest_streak_ending_here[j] >= max_len:
                    max_len = longest_streak_ending_here[j] + 1
                                
            longest_streak_ending_here[i] = max_len
        
        # Work backwards to find the longest subset and create array
        answer = []
        max_size = max_size_index = 0
        for i, size in enumerate(longest_streak_ending_here):
            if size > max_size:
                max_size = size
                max_size_index = i

        curr_size = max_size
        curr_tail = nums[max_size_index]
        # Work backwards appending entry each time
        for i in range(max_size_index, -1, -1):
            if curr_size == longest_streak_ending_here[i] and curr_tail % nums[i] == 0:
                answer.append(nums[i])
                curr_size -= 1
                curr_tail = nums[i]
        
        # Reverse the order
        answer.reverse()
        return answer

    # Sort nums then go over all nums
    # For every num see if it can be appended to the already created subsets
    # Return longest subset at the end
    # Time O(n^2) as for each index go through every index before it
    # Space O(n^2) as worst case entire array is same subset 
    def largestDivisibleSubset_memory_inefficient(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        # longest subset ending at this num
        subsets = [[]] * n
        
        # Go over every num and see if it can continue a subset
        for index, value in enumerate(nums):
            # Assume it can't append any already existing subsets
            nextEntry = [value]

            # Go over all previous subsets and see if this can append
            # Only append this num onto the longest already existing subset
            for j in range(index):
                if value % subsets[j][-1] == 0 and len(subsets[j]) >= len(nextEntry):
                    nextEntry = subsets[j].copy()
                    nextEntry.append(value)
                                
            subsets[index] = nextEntry
        
        # Find the longest subset and return it
        answer = []
        for subset in subsets:
            if len(subset) > len(answer):
                answer = subset
                
        return answer
    
testCases = [
    [[1,2,3], [1,2]],
    [[1,2,4,8], [1,2,4,8]]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.largestDivisibleSubset(nums)
    if expected != answer:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Input: {nums}")

print("Ran all tests")