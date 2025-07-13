from collections import Counter, defaultdict
from typing import List


class FindSumPairs:
    # Time O(n)
    # Space O(n)
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_count = Counter(nums1)
        self.nums2_count = Counter(nums2)
        self.nums2 = nums2

    # Time O(1)
    def add(self, index: int, val: int) -> None:
        self.nums2_count[self.nums2[index]] -= 1
        self.nums2_count[self.nums2[index] + val] += 1        
        self.nums2[index] += val

    # Time O(n)
    def count(self, tot: int) -> int:
        answer = 0

        for num, num1_count in self.nums1_count.items():
            target = tot - num
            if target in self.nums2_count:
                answer += (num1_count * self.nums2_count[target])

        return answer        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)