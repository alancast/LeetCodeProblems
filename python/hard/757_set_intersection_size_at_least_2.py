class Solution:
    # Time O(n^2)
    # Space O(n)
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        answer = 0
        a = b = -1

        for left, right in intervals:
            if left > b:
                a = right - 1
                b = right
                answer += 2
            elif left > a:
                a = b
                b = right
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
