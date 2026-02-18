class Solution:
    # Turns out you can math this
    # Time O(logk)
    # Space O(1)
    def kthCharacter(self, k: int) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1

        return chr(ord("a") + ans)

    # Brute force
    def kthCharacter_brute_force(self, k: int) -> str:
        word = "a"
        char_map = {'z': 'a'}
        while len(word) < k:
            next_word = []
            for char in word:
                if char in char_map:
                    next_word.append(char_map[char])
                else:
                    next_word.append(chr(ord(char) + 1))
            word += ''.join(next_word)

        return word[k-1]

test_cases = [
    ["b", 5],
    ["c", 10]
]
solution = Solution()
for expected, k in test_cases:
    actual = solution.kthCharacter(k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: k: {k}")

print("Ran all tests")
