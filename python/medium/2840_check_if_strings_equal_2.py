class Solution:
    # Just go over strings and count characters even and odd
    # Time O(n)
    # Space O(alphabet)
    # This is longer code to read to save memory (can be shorter with defaultdict)
    # One line version:
    # return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
    def checkStrings(self, s1: str, s2: str) -> bool:  # noqa: PLR0912
        n = len(s1)
        even_map = {}
        odd_map = {}

        # Add one for s1, sub 1 for s2
        for i in range(n):
            s1_char = s1[i]
            s2_char = s2[i]

            # Odd num
            if i & 1:
                if s1_char in odd_map:
                    odd_map[s1_char] += 1
                    if odd_map[s1_char] == 0:
                        del odd_map[s1_char]
                else:
                    odd_map[s1_char] = 1

                if s2_char in odd_map:
                    odd_map[s2_char] -= 1
                    if odd_map[s2_char] == 0:
                        del odd_map[s2_char]
                else:
                    odd_map[s2_char] = -1
            # Even num
            else:
                if s1_char in even_map:
                    even_map[s1_char] += 1
                    if even_map[s1_char] == 0:
                        del even_map[s1_char]
                else:
                    even_map[s1_char] = 1

                if s2_char in even_map:
                    even_map[s2_char] -= 1
                    if even_map[s2_char] == 0:
                        del even_map[s2_char]
                else:
                    even_map[s2_char] = -1


        # If either of them isn't empty then it's false
        return even_map == {} and odd_map == {}

test_cases = [
    [True, "abcdba", "cabdab"],
    [False, "abe", "bea"]
]
solution = Solution()
for expected, s1, s2 in test_cases:
    actual = solution.checkStrings(s1, s2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s1: {s1}, k: {s2}")

print("Ran all tests")
