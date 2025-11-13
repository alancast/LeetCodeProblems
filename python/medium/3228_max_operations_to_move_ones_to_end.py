class Solution:
    # To maximize you want to perform at the first usable 1 each time
    # Time O(n)
    # Space O(1)
    def maxOperations(self, s: str) -> int:
        n = len(s)
        answer = 0

        # Go over all chars in string
        i = 0
        ones_chain_size = 0
        while i < n:
            # Increment i until we find a 1 (or end of string)
            if s[i] == "0":
                while i + 1 < n and s[i + 1] == "0":
                    i += 1
                # Add to the answer however many ones in the current chain
                # E.g. how many ones do we need to move to this end
                answer += ones_chain_size
            # If it's a 1 add to the chain size
            else:
                ones_chain_size += 1

            i += 1

        return answer

test_cases = [
    [4, "1001101"],
    [0, "00111"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.maxOperations(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")