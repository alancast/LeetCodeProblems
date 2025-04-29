from typing import List


class Solution:
    # Basically same logic as below but much cleaner
    # Sliding window. See how many sub arrays can end at a given index
    # Then move left forward one and see how far right can go
    # Time O(n) as we go through the nums list just once
    # Space O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = sum = start = 0

        for end in range(n):
            sum += nums[end]

            # Find furthest left starting point we can
            while start <= end and sum * (end - start + 1) >= k:
                sum -= nums[start]
                start += 1

            count += end - start + 1
            
        return count


    # Sliding window. Start at an index and find as far as right index can go
    # Then move left forward one and see how far right can go
    # Time O(n) as we go through the nums list just once
    # Space O(1)
    def countSubarrays_uglier(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = right = sum = length = 0

        for i in range(n):
            while right < n and (sum * length) < k:
                sum += nums[right]
                right += 1
                length += 1

            # Figure out why loop broke and see if we need to decrement or can break
            if (sum * length) >= k:
                right -= 1
                sum -= nums[right]
                length -= 1
            # If right ever reaches the end and is valid all smaller subarrays
            # Will also work so can add at once with math and end
            else:
                combos_left = ((length)*(length + 1)) // 2
                count += combos_left
                break

            if length > 0:
                count += length

                # Move starting point right
                sum -= nums[i]
                length -= 1
            # If length is 0 that means right == i, so we need to move it forward too
            else:
                right += 1

        return count
    
test_cases = [
    [6, [2,1,4,3,5], 10],
    [0, [100], 10],
    [6, [1,1,100,1,1], 10],
    [6, [1,1,1], 10],
    [5, [1,1,1], 5]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.countSubarrays(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")