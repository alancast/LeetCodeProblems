from collections import deque, OrderedDict
from typing import List


# Keep set of unique, non unique, and ordered hash set queue
# Space O(n)
# Add O(1), showfirst O(1), constructor O(n)
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.numbersQueue = OrderedDict()
        self.uniqueNums = set()
        self.nonUniqueNums = set()
        
        # Populate queue and sets
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.numbersQueue:
            return next(iter(self.numbersQueue))

        return -1

    def add(self, value: int) -> None:
        # Number we've already seen multiple times
        if value in self.nonUniqueNums:
            return

        # Second time seeing this number, so it's no longer unique
        if value in self.uniqueNums:
            self.nonUniqueNums.add(value)
            self.uniqueNums.remove(value)
            self.numbersQueue.pop(value)
            return

        # New number, add to uniqueNums and queue
        self.numbersQueue[value] = None
        self.uniqueNums.add(value)
        
# Keep set of unique, non unique, and deque of queue
# Space O(n)
# Add O(1), showfirst O(1) amortized, but worst case O(n), constructor O(n)
class FirstUniqueAmortized:

    def __init__(self, nums: List[int]):
        self.numbersQueue = deque()
        self.uniqueNums = set()
        self.nonUniqueNums = set()
        
        # Populate queue and sets
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.numbersQueue:
            num = self.numbersQueue[0]
            
            # Number is not unique, remove it from the queue and try again
            if num in self.nonUniqueNums:
                self.numbersQueue.popleft()
                continue
            
            return num
        
        return -1

    def add(self, value: int) -> None:
        # Number we've already seen multiple times
        if value in self.nonUniqueNums:
            return

        # Second time seeing this number, so it's no longer unique
        if value in self.uniqueNums:
            self.nonUniqueNums.add(value)
            self.uniqueNums.remove(value)
            return

        # New number, add to uniqueNums and queue
        self.numbersQueue.append(value)
        self.uniqueNums.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)