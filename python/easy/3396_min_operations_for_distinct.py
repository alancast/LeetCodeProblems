from typing import List


class Solution:
    # Work backwards, as soon as we see first duplicate we know we must cut til there
    # Time O(n) goes over full array once potentially
    # Space O(n) potentially stores entire copy in dictionary
    def minimumOperations_backtrack(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            # We have a our final dupe, so do math to see how many operations to remove this
            if num in seen:
                return (i // 3) + 1
            # Haven't seen before so add to set
            else:
                seen.add(num)
        
        # If we get here it means we found no dupes, so no operations needed
        return 0
    
    # Time O(n) goes over array potentially twice
    # Space O(n) potentially stores entire copy in dictionary
    def minimumOperations_iterate_twice(self, nums: List[int]) -> int:
        num_operations = index_to_decrement = 0
        num_counter = dict()
        nums_to_remove = dict()

        # see how many of each num there is
        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
                nums_to_remove[num] = num_counter[num]
            else:
                num_counter[num] = 1

        # Perform operations until all distinct
        while len(nums_to_remove) > 0 and (index_to_decrement + 3) < len(nums):
            # "Remove" 3
            for i in range(3):
                num = nums[index_to_decrement]
                # We only care about the ones that are dupes
                if num in nums_to_remove:
                    nums_to_remove[num] -= 1
                    if nums_to_remove[num] == 1:
                        del nums_to_remove[num]

                index_to_decrement += 1
            
            num_operations += 1

        # see if in final 3 there is still dupes so another operation needed
        if len(nums_to_remove) > 0:
            num_operations += 1

        return num_operations
    
test_cases = [
    [0, [1]],
    [1, [1,1]],
    [1, [1,1,1]],
    [1, [1,1,1,1]],
    [0, [1,2,3,4,5,6]],
    [2, [1,2,3,1,2,3,1]],
    [1, [1,1,1,1,2,3]],
    [2, [4,5,6,1,1,1]],
    [2, [1,2,3,4,2,3,3,5,7]],
    [2, [4,5,6,4,4]],
    [0, [6,7,8,9]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumOperations_backtrack(nums)
    if actual != expected:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")