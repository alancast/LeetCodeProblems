from typing import List


class Solution:
    # There is a way to do this with math that is O(n)
    # Time O(n)
    # Space O(1)
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)-1

        answer = nums[0]
        sum_multiple = 1
    
        # Multiply each number by how many times it will be added to get sum
        for i in range(1, n+1):
            sum_multiple = (sum_multiple * (n-i+1))//i
            # Compute new sum
            answer = (answer + (nums[i] * sum_multiple)) % 10

        return answer

    # Modify array in place to save space. Just do the additions
    # Time O(n^2)
    # Space O(1)
    def triangularSum_brute(self, nums: List[int]) -> int:
        end = len(nums)

        while end > 0:
            for i in range(end-1):
                nums[i] += nums[i+1]
                nums[i] %= 10
            
            end -= 1

        return nums[0]

test_cases = [
    [8, [1,2,3,4,5]],
    [5, [5]],
    [5, [0,3,3,4,1,2,6,4,9,3,5,1,7,7,3,0,3,2,5,1,9,0,2,6,3,9,2,5,9,2,6,4,2,9,7,2,0,3,0,1,1,2,7,8,6,4,4,5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.triangularSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")