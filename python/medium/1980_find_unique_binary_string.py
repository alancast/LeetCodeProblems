from typing import List

class Solution:
    # Change one digit of each entry
    # by time you are at end you are sure to have num different from all other nums
    # Time O(n) where n is length of string. 
    # Space O(1) hash set of full nums
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        answer = []
        for i, num in enumerate(nums):
            if num[i] == '0':
                answer.append('1')
            else:
                answer.append('0')

        return ''.join(answer)

    # Create integer hash set from nums and iterate til we get one that isn't there
    # Worst case scenario the nums are the first n binary nums
    # Time O(n^2) where n is length of string. 
    # We go through n of them and convert them to int which takes n time
    # Space O(n) hash set of full nums
    def findDifferentBinaryString_slower(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set()
        for num in nums:
            num_set.add(int(num, 2))

        # Guaranteed to get a number not included if we just go to n + 1
        for i in range(n + 1):
            if i not in num_set:
                binary_str = bin(i)[2:].zfill(n)
                return binary_str
    
test_cases = [
    [set(["00", "11"]), ["01", "10"]],
    [set(["11", "10"]), ["00", "01"]],
    [set(["000", "010", "100", "110", "101"]), ["111", "011", "001"]]
]
solution = Solution()
for expecteds, nums in test_cases:
    actual = solution.findDifferentBinaryString(nums)
    if actual not in expecteds:
        print(f"FAILED TEST! Expected {expecteds} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")