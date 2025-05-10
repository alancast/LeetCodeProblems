from collections import defaultdict
from typing import List


class Solution:
    # Same logic as below way, but instead of binary search per index do precompute to make O(1)
    # T is len target S is len source
    # Time O(S+T) as worst case it's all the same char so each time search full map list
    # Space O(S) specifically 26*S
    def shortestWay(self, source: str, target: str) -> int:
        s = len(source)

        # Next Occurrence of Character after Index
        # 2D where first id is index and what is stored there is a map of char to next index
        next_occurrence = [defaultdict(int) for idx in range(s)]

        # Base Case (last index only has last letter)
        next_occurrence[s - 1][source[s - 1]] = s - 1

        # Using Recurrence Relation to fill next_occurrence
        # Row before last one is all that last one has plus whatever char is before that
        for idx in range(s - 2, -1, -1):
            next_occurrence[idx] = next_occurrence[idx + 1].copy()
            next_occurrence[idx][source[idx]] = idx

        count = 1
        source_iterator = 0
        # Find all characters of target in source
        for char in target:
            # If character is not in source, return -1
            if char not in next_occurrence[0]:
                return -1

            # If we have reached the end of source, or the character is not in
            # source after source_iterator, loop back to beginning
            if (source_iterator == s or char not in next_occurrence[source_iterator]):
                count += 1
                source_iterator = 0

            # Next occurrence of character in source after source_iterator
            source_iterator = next_occurrence[source_iterator][char] + 1

        # Return the number of times we need to iterate through source
        return count

    # Create a map of letter to indexes
    # Iterate over target as many chars as you can until need to start again
    # m is len target n is len source
    # Time O(n + m logn) as worst case it's all the same char so each time search full map list
    # Space O(n) as every index 
    def shortestWay_map_binary_search(self, source: str, target: str) -> int:
        # Key is char, value is list of indexes, increasing
        index_list_map = defaultdict(list[int])
        for i, char in enumerate(source):
            index_list_map[char].append(i)

        count = 1
        current_index = -1
        # Go through every char in target and see if it can be part of subsequence
        # Or if a new one is needed
        for char in target:
            # Make sure the char is in the source string
            if char not in index_list_map:
                return -1
            
            # See if it can be part of current substring
            index = self._smallest_index_above_x(index_list_map[char], current_index)
            # It is so can be part of same subsequence
            if index > current_index:
                current_index = index
            # it's not, so need to use new subsequence
            else:
                current_index = index_list_map[char][0]
                count += 1

        return count
    
    # Does binary search on indexes to find smallest index greater than index
    # Returns -1 if not possible
    def _smallest_index_above_x(self, sorted_indexes: List[int], index: int) -> int:
        left = 0
        right = len(sorted_indexes)

        while left < right:
            mid = ((left + right) // 2)
            if sorted_indexes[mid] > index:
                right = mid
            else:
                left = mid + 1

        # No index was above what was needed
        if left == len(sorted_indexes):
            return -1

        return sorted_indexes[left]
    
test_cases = [
    [2, "abc", "abcbc"],
    [-1, "abc", "acdbc"],
    [3, "xyz", "xzyxz"]
]
solution = Solution()
for expected, source, target in test_cases:
    actual = solution.shortestWay(source, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: source: {source}, target: {target}")

print("Ran all tests")