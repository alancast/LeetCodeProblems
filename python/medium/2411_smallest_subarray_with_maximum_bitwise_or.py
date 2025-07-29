from typing import List


class Solution:
    # Go backwards over array. Keep track of when each bit was set to 1
    # Time O(n*logc)
    # Space O(logc)
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Array for leftmost index of when this bit was switched to a 1
        # This will either be -1 if it's never been set to 1, or leftmost index it's set to
        pos = [-1] * 31

        answer = [0] * n
        # Start at last number and work backwards to first
        for i in range(n - 1, -1, -1):
            # Assume max bitwise or is just this number until proven otherwise
            end_index = i

            # Go over all the bits in number
            # If one is a 0 and it's a 1 in a later number, then it's needed for max
            # So get index of that number and go forward
            for bit in range(31):
                # If this bit is zero
                if (nums[i] & (1 << bit)) == 0:
                    # If this bit is 1 somewhere after this in the array, update end_index
                    if pos[bit] != -1:
                        end_index = max(end_index, pos[bit])
                # If this bit is 1, set the positions array to this index
                else:
                    pos[bit] = i
            
            # Update min subset for this index
            answer[i] = end_index - i + 1

        return answer
    
    # Brute force way. Will exceed time limit
    # Time O(n^2)
    # Space O(1)
    def smallestSubarrays_brute_force(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n):
            bitwise_or = nums[i]
            max = 1
            for j in range(i+1, n):
                num_j = nums[j]
                next_or = bitwise_or | num_j

                if next_or > bitwise_or:
                    max = j - i + 1

                bitwise_or = next_or

            answer.append(max)

        return answer
    
test_cases = [
    [[3,3,2,2,1], [1,0,2,1,3]],
    [[2,1], [1,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.smallestSubarrays(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")