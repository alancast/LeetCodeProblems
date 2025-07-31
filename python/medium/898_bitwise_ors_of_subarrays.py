from typing import List


class Solution:
    # Time O(n*b) where b is number of bits in max num and n is number of nums
    # Space O(n*b)
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # This set will store all unique OR values found across all subarrays.
        result_ors = set()
        
        # This set stores the distinct ORs of all subarrays ending at the previous position.
        current_ors = set()

        # Iterate through each element of the array.
        for num in arr:
            # Find the ORs of all subarrays ending at this num
            # Do this by OR-ing this num with all subarrays ending at last num
            next_ors = set()
            for other_num in current_ors:
                next_ors.add(other_num | num)

            # Also add the num itself
            next_ors.add(num)
            
            # Add all newly found ORs to the answer set
            result_ors.update(next_ors)
            
            # Update current ors for next num
            current_ors = next_ors
            
        # The number of different options is just the size of this set
        return len(result_ors)
    
test_cases = [
    [1, [0]],
    [3, [1,1,2]],
    [6, [1,2,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.subarrayBitwiseORs(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")