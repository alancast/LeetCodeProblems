class Solution:
    # Go over each char and store ord value
    # As soon as we see other case of it, increment count
    # Time O(n)
    # Space O(n)
    def numberOfSpecialChars(self, word: str) -> int:
        # Some special chars making it not be 26
        ALPHABET_SIZE = 32
        answer = 0

        seen_nums = {}
        for char in word:
            # Already seen this char so no need to carry on
            if ord(char) in seen_nums:
                continue

            # Set this num to seen
            seen_nums[ord(char)] = 1

            lower = ord(char) + ALPHABET_SIZE
            if lower in seen_nums:
                if seen_nums[lower] != 1:
                    continue

                # It does equal one so a new special char is found
                answer += 1
                # Set values so we don't count it in the future
                seen_nums[ord(char)] = 2
                seen_nums[lower] = 2
                continue

            upper = ord(char) - ALPHABET_SIZE
            if upper in seen_nums:
                if seen_nums[upper] != 1:
                    continue

                # It does equal one so a new special char is found
                answer += 1
                # Set values so we don't count it in the future
                seen_nums[ord(char)] = 2
                seen_nums[upper] = 2
                continue

        return answer

test_cases = [
    [3, "aaAbcBC"],
    [0, "abc"],
    [1, "abBCab"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.numberOfSpecialChars(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")
