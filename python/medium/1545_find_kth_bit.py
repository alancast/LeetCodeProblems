class Solution:
    # Bit manipulation solution I would not have come up with
    # Time O(1)
    # Space O(1)
    def findKthBit(self, n: int, k: int) -> str:
        # Find the position of the rightmost set bit in k
        # This helps determine which "section" of the string we're in
        position_in_section = k & -k

        # Determine if k is in the inverted part of the string
        # This checks if the bit to the left of the rightmost set bit is 1
        is_in_inverted_part = ((k // position_in_section) >> 1 & 1) == 1

        # Determine if the original bit (before any inversion) would be 1
        # This is true if k is even (i.e., its least significant bit is 0)
        original_bit_is_one = (k & 1) == 0

        if is_in_inverted_part:
            # If we're in the inverted part, we need to flip the bit
            return "0" if original_bit_is_one else "1"

        # If we're not in the inverted part, return the original bit
        return "1" if original_bit_is_one else "0"

    # Iterative solution
    # Time O(n)
    # Space O(1)
    def findKthBit_iterative(self, n: int, k: int) -> str:
        # How many times the bit we are looking for has been inverted
        invert_count = 0
        # Length of Sn is 2^n - 1
        length = (1 << n) - 1

        while k > 1:
            # If k is in the middle, return based on inversion count
            if k == length // 2 + 1:
                return "1" if invert_count % 2 == 0 else "0"

            # If k is in the second half, invert and mirror
            if k > length // 2:
                # Mirror position
                k = length + 1 - k
                invert_count += 1

            # Reduce length for next iteration
            # if k was in first half nothing else needed
            length //= 2

        # For the first position, return based on inversion count
        return "0" if invert_count % 2 == 0 else "1"

    # Brute force method just compute first n strings then return kth bit
    # Time O(2^n)
    # Space O(2^n)
    def findKthBit_brute(self, n: int, k: int) -> str:
        string = "0"

        # Compute string
        for _ in range(1, n+1):
            # Start never changes, only adds on
            if len(string) >= k:
                return string[k-1]

            string = string + "1" + self._reverse_invert(string)

        return string[k-1]

    # Returns the reverse inverted string
    def _reverse_invert(self, s: str) -> str:
        n = len(s)

        rev_inv = ""
        for i in range(n):
            rev_inv += "1" if s[-(i + 1)] == "0" else "0"

        return rev_inv

test_cases = [
    ["0", 3, 1],
    ["1", 4, 11]
]
solution = Solution()
for expected, n, k in test_cases:
    actual = solution.findKthBit(n, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, k: {k}")

print("Ran all tests")
