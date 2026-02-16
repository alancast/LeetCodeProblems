class Solution:
    # Create set of broken letters,
    # then just go over words and count ones that aren't broken
    # Time O(n)
    # Space O(n)
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Create set of letters that are broken (for easier access)
        bad_letters = set()
        for char in brokenLetters:
            bad_letters.add(char)

        answer = 0
        # Go over all (both) words and see if they are doable
        words = text.split(' ')
        for word in words:
            can_use = 1
            # Go over each letter in each word
            for char in word:
                if char in bad_letters:
                    can_use = 0
                    break

            answer += can_use

        return answer

test_cases = [
    [1, "hello world", "ad"],
    [1, "leet code", "lt"],
    [0, "leet code", "e"]
]
solution = Solution()
for expected, text, broken_letters in test_cases:
    actual = solution.canBeTypedWords(text, broken_letters)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: text: {text}, broken_letters: {broken_letters}")

print("Ran all tests")
