class Solution:
    # Just compute running sum and take max
    # Time O(n)
    # Space O(1)
    def largestAltitude(self, gain: list[int]) -> int:
        answer = running_total = 0

        for num in gain:
            running_total += num
            answer = max(answer, running_total)

        return answer

test_cases = [
    [1, [-5,1,5,0,-7]],
    [0, [-4,-3,-2,-1,4,3,2]]
]
solution = Solution()
for expected, gain in test_cases:
    actual = solution.largestAltitude(gain)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: gain: {gain}")

print("Ran all tests")
