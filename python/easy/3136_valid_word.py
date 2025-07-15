class Solution:
    # Time O(n) as we go over the word once
    # Space O(1)
    def isValid(self, word: str) -> bool:
        length = 0
        vowel = consonant = False

        for char in word:
            length += 1
            # Not an alphanumeric char
            if not char.isalnum():
                return False
            
            # Don't care about digits
            if char.isdigit():
                continue

            char = char.lower()
            if char in 'aeiou':
                vowel = True
            else:
                consonant = True

        return length >= 3 and vowel and consonant
    
test_cases = [
    [True, "234Adas"],
    [False, "b3"],
    [False, "a3$e"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.isValid(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")