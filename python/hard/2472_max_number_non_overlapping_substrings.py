class Solution:
    # Greedily select first palindrome of length k+ with earliest ending
    # Time O(nk)
    # Space O(1)
    def maxPalindromes(self, s: str, k: int) -> int:
        # See if the string is a palindrome
        def check(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        answer = 0
        start = 0

        # Go over all end indexes and find palindromes (check for even and odd lengths)
        for end_index in range(k - 1, n):
            # Check for even and odd lengths
            # If this is a palindrome, move start to after the end of this
            start_index = end_index - k + 1
            if start_index >= start and check(start_index, end_index):
                answer += 1
                start = end_index + 1
                continue

            # If this is a palindrome, move start to after the end of this
            start_index = end_index - k
            if start_index >= start and check(start_index, end_index):
                answer += 1
                start = end_index + 1

        return answer

test_cases = [
    [2, "abaccdbbd", 3],
    [0, "adbcda", 2]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.maxPalindromes(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")
