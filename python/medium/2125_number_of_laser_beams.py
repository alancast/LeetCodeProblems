from typing import List


class Solution:
    # For each row count number of ones
    # Just multiply by previous number with ones and sum it all
    # Time O(n*m)
    # Space O(1)
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = prev_ones = 0

        for row in bank:
            ones = row.count("1")
            if ones:
                answer += (ones * prev_ones)
                prev_ones = ones

        return answer

test_cases = [
    [8,["011001","000000","010100","001000"]],
    [0, ["000","111","000"]]
]
solution = Solution()
for expected, bank in test_cases:
    actual = solution.numberOfBeams(bank)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: bank: {bank}")

print("Ran all tests")
