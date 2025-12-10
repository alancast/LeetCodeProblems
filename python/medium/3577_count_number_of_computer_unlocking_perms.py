from typing import List


class Solution:
    MOD = 10**9 + 7

    # Stupid just brain teaser
    # Either complexity 0 isn't the lowest so the answer is 0
    # Or it is the lowest and then the answer is just n-1 factorial
    # Time O(n)
    # Space O(1)
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # Make sure all computer can be unlocked
        for i in range(1,n):
            # This computer can never be unlocked
            if complexity[i] <= complexity[0]:
                return 0

        # All computers can be unlocked so just do the math
        answer = 1
        for i in range(2, n):
            answer = answer * i % self.MOD

        return answer

test_cases = [
    [2, [1,2,3]],
    [0, [3,3,3,4,4,4]]
]
solution = Solution()
for expected, complexity in test_cases:
    actual = solution.countPermutations(complexity)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: complexity: {complexity}")

print("Ran all tests")