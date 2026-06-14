class Solution:
    # Just do the computations for each one
    # Time O(n)
    # Space O(1)
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        answer = []

        # Go over all words
        for word in words:
            # Go over all chars in word and add up sum
            word_sum = 0
            for c in word:
                word_sum += weights[ord(c) - ord("a")]

            # Add the mapped char to the array
            answer.append(chr(ord("z") - word_sum % 26))

        return "".join(answer)

test_cases = [
    ["rij", ["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]],
    ["yyy", ["a","b","c"], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
    ["g", ["abcd"], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]]
]
solution = Solution()
for expected, words, weights in test_cases:
    actual = solution.mapWordWeights(words, weights)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words: {words}, weights: {weights}")

print("Ran all tests")
