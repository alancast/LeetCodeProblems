class Solution:
    # Iterate over all ending spots and see how many substrings can end there
    # Make array of indices of 0's prior to current index
    # Time O(n sqrt(n))
    # Space O(n) for array of previous zeros
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        # Array of all 0's before this index 
        # one longer than string for right bounding
        previous_zero_idx = [-1] * (n + 1)
        for i in range(n):
            # If this is start or a zero set next one to this index
            if i == 0 or s[i - 1] == "0":
                previous_zero_idx[i + 1] = i
            # If this is a 1 carry forward the previous zero
            else:
                previous_zero_idx[i + 1] = previous_zero_idx[i]

        answer = 0
        # Go over all right bounds of possible strings
        for i in range(1, n + 1):
            count_zeros = 1 if s[i - 1] == "0" else 0
            j = i

            # Keep going backwards until too many zeros
            while j > 0 and count_zeros * count_zeros <= n:
                count_ones = (i - previous_zero_idx[j]) - count_zeros
                # If this is a 1 dominated string add how many this adds
                if count_zeros * count_zeros <= count_ones:
                    # Formula for how many substrings this adds
                    answer += min(j - previous_zero_idx[j], count_ones - (count_zeros * count_zeros) + 1)
                
                # Move j backwards and add another zero
                j = previous_zero_idx[j]
                count_zeros += 1

        return answer

test_cases = [
    [5, "00011"],
    [16, "101101"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.numberOfSubstrings(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")