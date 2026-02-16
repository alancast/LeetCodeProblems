class Solution:
    # Time O(n) as we go through the full string once
    # Space O(n) as we create array from string (could argue O(1))
    def makeFancyString(self, s: str) -> str:
        if not s:
            return ""

        prev = s[0]
        answer = [prev]
        count = 1
        n = len(s)

        # Go over every character and see if it should be added to string or not
        for i in range(1, n):
            char = s[i]
            # See if this is 3rd or more and update count
            if char == prev:
                count += 1
            else:
                count = 1

            # Add char to string
            if count < 3:  # noqa: PLR2004
                answer.append(char)

            # Prep for next iteration
            prev = char

        return ''.join(answer)

    # A way to do in place if memory super tight,
    # but doesn't benefit in python as strings are immutable in python
    # Time O(n)
    # Space O(1) if string was mutable
    def makeFancyString_space_concern(self, s: str) -> str:
        # If size of string is less than 3, return it.
        if len(s) < 3:  # noqa: PLR2004
            return s

        # Convert the string to a list for mutability.
        # This is why this is pointless in python
        s_list = list(s)
        j = 2

        # Iterate through the string from index 2.
        for i in range(2, len(s)):
            # If the current character is not equal to the previously inserted
            # two characters, then we can add it to the result.
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        # Resize the list to the number of valid characters and join it back into a string.
        return "".join(s_list[:j])

test_cases = [
    ["leetcode", "leeetcode"],
    ["aabaa", "aaabaaaa"],
    ["aab", "aab"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.makeFancyString(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
