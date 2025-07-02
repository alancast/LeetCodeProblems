class Solution:
    MOD = 10**9 + 7

    # Time O(n+k^2)
    # Space O(n + k) as copy letter frequencies could be all 1's + k
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        count = 1
        letter_frequencies = []

        # Create list of letter frequencies of letters
        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                letter_frequencies.append(count)
                count = 1
        # Make sure get last characters
        letter_frequencies.append(count)

        # Now do math for answer
        # Assume that every frequency can be downsized to 1
        answer = 1
        for freq in letter_frequencies:
            answer = answer * freq % self.MOD

        # If number of duplicates is greater than k than our assumption
        # Of being able to downsize to 1 is true, so just return answer
        if len(letter_frequencies) >= k:
            return answer

        # Now go through all possibilities of where downsizing to 1 isn't possible
        # Iterate over all the frequencies and make combinations if they are downsized
        f = [1] + [0] * (k - 1)
        g = [1] * k
        for i in range(len(letter_frequencies)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - letter_frequencies[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - letter_frequencies[i] - 1]) % self.MOD

            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % self.MOD

            f = f_new
            g = g_new
        
        # Return answer
        return (answer - g[k - 1]) % self.MOD
    
test_cases = [
    [5, "aabbccdd", 7],
    [1, "aabbccdd", 8],
    [8, "aaabbb", 3]
]
solution = Solution()
for expected, word, k in test_cases:
    actual = solution.possibleStringCount(word, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: word: {word}, k: {k}")

print("Ran all tests")