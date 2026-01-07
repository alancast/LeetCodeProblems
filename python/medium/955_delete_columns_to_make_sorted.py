from typing import List


class Solution:
    # Go column by column and make sure sorted
    # As soon as we don't need to delete a column no others matter
    # Time O(n*m) where m is length of strings
    # Space O(n)
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        # See if this index is sorted with regard to it's neighbor
        sorted_pairs = [False] * (n - 1)
        cols = len(strs[0])

        answer = 0
        # Go column by column and make sure it's all sorted
        for col in range(cols):
            not_sorted = False
            for i in range(n - 1):
                # If these two are still in consideration and this col is not sorted
                # Then this col must be deleted
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    not_sorted = True
                    break

            # If this column wasn't sorted then no ties matter, so on to next col
            if not_sorted:
                answer += 1
                continue

            # Go over all indexes and see if this is sorted now
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

            # If they are all sorted then nothing after matters, we have answer
            if all(sorted_pairs):
                break

        return answer

test_cases = [
    [1, ["ca","bb","ac"]],
    [0, ["xc","yb","za"]],
    [3, ["zyx","wvu","tsr"]]
]
solution = Solution()
for expected, strs in test_cases:
    actual = solution.minDeletionSize(strs)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: strs: {strs}")

print("Ran all tests")
