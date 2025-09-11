class Solution:
    # Go over string and count vowels, then go over string again and replace
    # Time O(n) for indexing then sorting then replacing
    # Space O(10)
    def sortVowels(self, s: str) -> str:
        vowels = [0] * 10
        answer = []

        # Find vowels and update index counts
        for char in s:
            answer.append(char)
            index = self._is_vowel(char)
            if index >= 0:
                vowels[index] += 1

        # Go over string again and update vowels
        unused_index = 0
        for i, char in enumerate(answer):
            vowel_index = self._is_vowel(char)

            # If we have a vowel replace with whatever highest sorted one is left
            if vowel_index >= 0:
                # Find what vowel type is left
                while vowels[unused_index] == 0:
                    unused_index += 1

                # Swap to that vowel and decrement count
                answer[i] = self._convert_to_vowel(unused_index)
                vowels[unused_index] -= 1

        return "".join(answer)

    def _is_vowel(self, char: str) -> int:
        return "AEIOUaeiou".find(char)

    def _convert_to_vowel(self, index: int) -> str:
        return "AEIOUaeiou"[index]

    # Create array of chars, then index vowels and sort them, then replace
    # Time O(n + nlogn + n) for indexing then sorting then replacing
    # Space O(n) for sort and storing copy
    def sortVowels_sort(self, s: str) -> str:
        vowels = []
        answer = []

        for char in s:
            answer.append(char)
            if char in "AEIOUaeiou":
                vowels.append(char)
        
        vowels.sort(reverse=True)

        for i, char in enumerate(answer):
            if char in "AEIOUaeiou":
                answer[i] = vowels[-1]
                vowels.pop()

        return "".join(answer)

test_cases = [
    ["lEOtcede", "lEetcOde"],
    ["lYmpH", "lYmpH"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.sortVowels(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")