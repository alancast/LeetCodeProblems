from typing import List


class Solution:
    # Time O(n^2)
    # Space O(n)
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        answer = 0
        a = b = -1

        for l, r in intervals:
            if l > b:
                a = r - 1
                b = r
                answer += 2
            elif l > a:
                a = b
                b = r
                answer += 1

        return answer

test_cases = [
    [5, [[1,3],[3,7],[8,9]]],
    [3, [[1,3],[1,4],[2,5],[3,5]]],
    [5, [[1,2],[2,3],[2,4],[4,5]]]
]
solution = Solution()
for expected, intervals in test_cases:
    actual = solution.intersectionSizeTwo(intervals)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: intervals: {intervals}")

print("Ran all tests")
