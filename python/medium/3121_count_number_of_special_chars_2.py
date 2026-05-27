class Solution:
    # Basically same idea as below, just more pythonic, not storing ord
    # Keep indices of all lower and first upper and then just check
    # Time O(n)
    # Space O(n)
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        # Track indexes of answers
        for i, char in enumerate(word):
            # Store last index of lower
            if char.islower():
                lower[char] = i
            # Store only first index of upper
            elif char not in upper:
                upper[char] = i

        # Go over indexes and find answer
        answer = 0
        for key, val in lower.items():
            cap = key.upper()
            # Only count if upper is after this
            if cap in upper and val < upper[cap]:
                answer +=1

        return answer

    # Go over each char and store ord value
    # Have values for state and only count valid ones
    # Time O(n)
    # Space O(n)
    def numberOfSpecialChars_harder_to_read(self, word: str) -> int:
        # Some special chars making it not be 26
        ALPHABET_SIZE = 32
        # Constants for state
        SEEN = 1
        COUNTED = 2
        INVALID = 3
        answer = 0

        seen_nums = {}
        for char in word:
            char_ord = ord(char)
            # ORD goes ABC...abc
            lower = ord(char) + ALPHABET_SIZE
            upper = ord(char) - ALPHABET_SIZE

            # If it's already invalid carry on
            if char_ord in seen_nums and seen_nums[char_ord] == INVALID:
                continue

            # If we've already seen the upper of this make sure it's no longer counted
            if upper in seen_nums:
                # If it was already counted, redact it
                if char_ord in seen_nums and seen_nums[char_ord] == COUNTED:
                    answer -= 1

                # Set upper and this to be invalid now
                seen_nums[char_ord] = INVALID
                seen_nums[upper] = INVALID
                continue

            # This is an upper and we have seen lower (but not yet counted)
            if lower in seen_nums and seen_nums[lower] == SEEN:
                answer += 1
                seen_nums[lower] = COUNTED
                seen_nums[char_ord] = COUNTED
                continue

            # Set char as seen as this is last option left
            seen_nums[char_ord] = SEEN

        return answer

test_cases = [
    [3, "aaAbcBC"],
    [0, "abc"],
    [0, "AbBCab"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.numberOfSpecialChars(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")
