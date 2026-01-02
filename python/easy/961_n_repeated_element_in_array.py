from typing import List


class Solution:
    # Less space efficient but more memory efficient
    # Since half of array is one num, then at least one set of 4
    # Must have a dupe. Once you find that it's your answer
    # So go over array and compare with neighbor, then compare with 2 and 3 hop
    # Time O(n) specifically 3n
    # Space O(1)
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)

        # Check neighbors then ones one apart
        for jump in range(1,4):
            # See if they are same
            for i in range(n-jump):
                if nums[i] == nums[i+jump]:
                    return nums[i]

        # Will never get here
        return -1
    
    # Set of seen numbers, as soon as dupe is seen that's answer
    # Time O(n)
    # Space O(n)
    def repeatedNTimes_set(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            
            seen.add(num)
        
        # This will never happen
        return -1

    # Keep a count of current number, as soon as it hits 0 switch it
    # Time O(n)
    # Space O(1)
    def repeatedNTimes_requires_n_plus_one(self, nums: List[int]) -> int:
        curr_num = nums[0]
        curr_count = 0

        for num in nums:
            if num == curr_num:
                curr_count += 1
            else:
                curr_count -= 1
            
            # If the old num is down to 0, switch it to the new num
            if curr_count <= 0:
                curr_num = num
                curr_count = 1

        return curr_num

test_cases = [
    [3, [1,2,3,3]],
    [2, [2,1,2,5,3,2]],
    [5, [5,1,5,2,5,3,5,4]],
    [9, [9,4,5,9]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.repeatedNTimes(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")