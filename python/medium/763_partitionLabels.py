from typing import List


class Solution():
    # Go through string and find last index, then go through again updating last each time
    # Time O(n) as we go through string twice
    # Space O(1) as we store a map of 26 entries
    def partitionLabels(self, s: str) -> List[int]:
        # Map of char to last index for it
        last_index_map = dict()
        for i, char in enumerate(s):
            last_index_map[char] = i

        # Go through and as soon as we get to end of substring append it
        answer = []
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, last_index_map[char])
            if i == end:
                answer.append(end - start + 1)
                start = i + 1
            
        return answer

testCases = [
    ["ababcbacadefegdehijhklij", [9,7,8]],
    ["abc", [1,1,1]],
    ["eccbbbbdec", [10]]
]
implementation = Solution()
for s, expected in testCases:
    answer = implementation.partitionLabels(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {s}")

print("Ran all tests")