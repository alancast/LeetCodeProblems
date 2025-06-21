from collections import Counter


class Solution:
    # Kinda confusing logic but basically go over all chars assuming it's the min
    # And see how many deletions needed to make it special if it's the min
    # Whichever one produces lowest deletion number use that as the min char
    # Time O(n + alphabet_size^2) as we go over the string once but then all chars n2
    # Space O(alphabet_size)
    def minimumDeletions(self, word: str, k: int) -> int:
        char_counts = Counter(word)

        # Worst case scenario delete entire word
        answer = len(word)

        # Go through every char assuming it's min, and assess deletion from there
        # Pick first char
        for a in char_counts.values():

            deleted = 0
            # See how many deleted if this is min char
            for b in char_counts.values():
                # Remove all b (to make sure a is min)
                if a > b:
                    deleted += b
                # Remove enough b to put it in range of a + k
                elif b > a + k:
                    deleted += b - (a + k)
                # else none need to be deleted

            # See if this a char produced a lower deletion number than previous ones
            answer = min(answer, deleted)
    
        return answer
    
test_cases = [
    [3, "aabcaba", 0],
    [5, "abbbbbbbbbccccc", 0],
    [2, "dabdcbdcdcd", 2],
    [1, "aaabaaa", 2]
]
solution = Solution()
for expected, word, k in test_cases:
    actual = solution.minimumDeletions(word, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: word: {word}, k: {k}")

print("Ran all tests")