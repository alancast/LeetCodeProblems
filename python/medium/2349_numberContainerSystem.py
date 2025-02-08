from collections import defaultdict
import heapq


# Implementation with two maps and lazy find
# Find O(klogn), change O(logn)
class NumberContainers:

    def __init__(self):
        self.numberMap = defaultdict(list)
        self.indexMap = defaultdict(int)

    # Time O(logn)
    def change(self, index: int, number: int) -> None:
        # Update index to number mapping
        self.indexMap[index] = number

        # Add index to the min heap for this number
        heapq.heappush(self.numberMap[number], index)

    # Time O(klogn)
    def find(self, number: int) -> int:
        # If number doesn't exist in our map
        if not self.numberMap[number]:
            return -1

        # Keep checking top element until we find valid index (that wasn't changed)
        while self.numberMap[number]:
            index = self.numberMap[number][0]

            # If index still maps to our target number, return it
            if self.indexMap[index] == number:
                return index

            # Otherwise remove this stale index
            heapq.heappop(self.numberMap[number])
        # potential the number no longer exists as they were all changed
        return -1

# Implementation with two maps and no lazy work
# Find O(1), change O(nlogn)
class NumberContainersNotLazy:

    def __init__(self):
        self.numberMap = defaultdict(list)
        self.indexMap = defaultdict(int)

    # Time O(nlogn)
    def change(self, index: int, number: int) -> None:
        # See if number already at index
        if index in self.indexMap:
            # Make sure it's a real change
            if self.indexMap[index] == number:
                return
            
            # Update numberMap for what was there O(nlogn)
            self.removeIndexFromNumberMap(index, self.indexMap[index])
            # add number at index
            self.indexMap[index] = number
            # update numberMap for that number O(nlogn)
            self.addIndexToNumberMap(index, number)
        # Nothing at index currently
        else:
            # Add number to index
            self.indexMap[index] = number
            # Update number
            self.addIndexToNumberMap(index, number)

    # Time O(1)
    def find(self, number: int) -> int:
        if number in self.numberMap:
            return self.numberMap[number][0]

        return -1

    def removeIndexFromNumberMap(self, index: int, number:int) -> None:
        self.numberMap[number].remove(index)
        # Check if list is now empty
        if len(self.numberMap[number]) == 0:
            self.numberMap.pop(number)
        
    def addIndexToNumberMap(self, index: int, number:int) -> None:
        # Number not in number map
        if number not in self.numberMap:
            self.numberMap[number] = [index]
        # Number already in number map
        else:
            self.numberMap[number].append(index)
            self.numberMap[number].sort()        