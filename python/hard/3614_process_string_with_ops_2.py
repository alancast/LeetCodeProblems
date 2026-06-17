class Solution:
    # Work backwards. See what k maps back to in first version of s
    # Compute length of final string, then see what it maps to
    # Time O(n)
    # Space O(1)
    def processStr(self, s: str, k: int) -> str:  # noqa: PLR0912
        # Compute the length of what the final string will be
        length = 0
        for char in s:
            # Removes last char, so shrink length
            if char == "*":
                if length:
                    length -= 1
            # Duplicates length of string
            elif char == "#":
                length *= 2
            # Reverses s, but we don't care about that because purely computing length
            elif char == "%":
                pass
            # Just adds a char
            else:
                length += 1

        # K won't be in the string so return the "."
        if k + 1 > length:
            return "."

        # K is in the final string, so figure out what it is
        # Must reverse s because we go from back to front for this computation
        for char in reversed(s):
            # This would have removed a char, so add to length
            if char == "*":
                length += 1
            # This would have duplicated, so instead cut in half
            elif char == "#":
                if k + 1 > (length + 1) // 2:
                    k -= length // 2
                length = (length + 1) // 2
            # This reverses, so go to other side of string
            elif char == "%":
                k = length - k - 1
            # We either have the character or move backward one
            else:
                if k + 1 == length:
                    return char
                length -= 1

        return "."

test_cases = [
    ["a", "a#b%*", 1],
    ["d", "cd%#*#", 3],
    [".", "z*#", 0]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.processStr(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}, k: {k}")

print("Ran all tests")
