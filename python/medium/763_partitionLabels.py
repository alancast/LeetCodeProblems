from typing import List


class Solution():
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        j = 0
        start = 0
        answer = []

        # Range must include last occurrance of this letter
        # Make sure that all letters in between are included too
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                answer.append(i - start + 1)
                start = i + 1
            
        return answer

testCases = [
    ["ababcbacadefegdehijhklij", [9,7,8]],
    ["eccbbbbdec", [10]]
]
implementation = Solution()
for s, expected in testCases:
    answer = implementation.partitionLabels(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {s}")