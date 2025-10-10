from typing import List


class Solution:
    # Go backwards from last k entries in energy
    # Time O(n)
    # Space O(1)
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        answer = float('-inf')

        # Last k entries in array
        for i in range(n - k, n):
            # Set total and work backwards
            total = 0
            j = i
            # Go until we get to start of array
            while j >= 0:
                total += energy[j]
                # See if this is new max total
                answer = max(answer, total)
                j -= k

        return answer

test_cases = [
    [3, [5,2,-10,-5,1], 3],
    [-1, [-2,-3,-1], 2]
]
solution = Solution()
for expected, energy, k in test_cases:
    actual = solution.maximumEnergy(energy, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: energy: {energy}, k: {k}")

print("Ran all tests")