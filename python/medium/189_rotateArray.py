from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return
        
        N = len(nums)
        k %= N
        if k == 0:
            return

        # Count is to keep track of how many numbers we've swapped
        # We need to swap each one
        start_idx = count = 0
        while count < N:
            # Chain swap until we get back to start, then iterate start
            current_idx, prev = start_idx, nums[start_idx]
            while True:
                next_idx = (current_idx + k) % N
                nums[next_idx], prev = prev, nums[next_idx]
                current_idx = next_idx
                count += 1
                
                if start_idx == current_idx:
                    break
            
            # Iterate swap
            start_idx += 1

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotateReverse(self, nums: List[int], k: int) -> None:
        if not nums:
            return 

        N = len(nums)
        k %= N

        self.reverse(nums, 0, N - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, N - 1)

testCases = [
    [[1,2,3,4], 2, [3,4,1,2]],
    [[1,2,3,4], 6, [3,4,1,2]],
    [[1,2,3], 1, [3,1,2]],
    [[], 1, []],
    [[1,2,3], 3, [1,2,3]],
    [[1,2,3], 0, [1,2,3]],
    [[1,2,3,4,5,6,7,8], 3, [6,7,8,1,2,3,4,5]]
]
solution = Solution()
for nums, k, expected in testCases:
    answer = nums.copy()
    solution.rotate(answer, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Inputs: {nums}, {k}")
