class Solution:
    # Can just do with math
    # Time O(log(n))
    # Space O(1)
    def getHappyString(self, n: int, k: int) -> str:
        self.validate_input(n, k)
        # Number of possible combinations is 3 * 2^(n-1)
        possible_strings_left = 3 * pow(2, n-1)
        if k > possible_strings_left:
            return ""

        answer = str()
        # Can find the first character by seeing which 3rd of possible options k is in
        # Then update k for new search space
        if k > (2 * (possible_strings_left // 3)):
            answer += "c"
            k -= (2 * (possible_strings_left // 3))
        elif k > (possible_strings_left // 3):
            answer += "b"
            k -= (possible_strings_left // 3)
        else:
            answer += "a"
        # Update possible strings left to reflect new search subspace
        possible_strings_left //= 3

        # Can build the string character by character
        # This new search space it's either upper half or lower half
        lower_chars = {"a": "b", "b": "a", "c": "a"}
        higher_chars = {"a": "c", "b": "c", "c": "b"}
        while possible_strings_left > 1:
            if k > (possible_strings_left//2):
                answer += higher_chars[answer[-1]]
                k -= (possible_strings_left//2)
            else:
                answer += lower_chars[answer[-1]]

            possible_strings_left //= 2

        return answer
    
    def validate_input(self, n: int, k: int) -> None:
        if n < 1 or n > 10:
            raise ValueError("n must be between 1 and 10")
        if k < 1 or k > 100:
            raise ValueError("k must be between 1 and 100")

test_cases = [
    ["abacbabacb", 10, 100],
    ["c", 1, 3],
    ["", 1, 4],
    ["cab", 3, 9]
]
solution = Solution()
for expected, n, k in test_cases:
    actual = solution.getHappyString(n, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}, k: {k}")

print("Ran all tests")