class Solution:
    # Time O(log n * log n)
    # Space O(1)
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1

        return curr

    # To count how many numbers exist between prefix1 and prefix2
    def _count_steps(self, n: int, prefix1: int, prefix2: int) -> int:
        steps = 0

        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10

        return steps

    # Time O(k)
    # Space O(1)
    def findKthNumber_k_time(self, n: int, k: int) -> int:
        current_num = 1
        for _ in range(k-1):
            # if times 10 is still smaller then multiply by 10
            if current_num * 10 <= n:
                current_num *= 10
            # Otherwise increment digit by 1
            else:
                while current_num % 10 == 9 or current_num >= n:
                    current_num //= 10
                current_num += 1

        return current_num
    
test_cases = [
    [2, 10, 3],
    [10, 13, 2],
    [1, 1, 1]
]
solution = Solution()
for expected, n, k in test_cases:
    actual = solution.findKthNumber(n, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}, k: {k}")

print("Ran all tests")