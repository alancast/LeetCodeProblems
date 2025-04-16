from heapq import heappop, heappush


class SuperSequenceQueueItem:
    def __init__(self, string_sequence: str, str1_index: int, str2_index: int):
        self.string_sequence = string_sequence
        self.str1_index = str1_index
        self.str2_index = str2_index

    def __lt__(self, other):
        # Custom comparison for priority queue
        return len(self.string_sequence) < len(other.string_sequence)


class Solution:
    # Faster DP algorithm
    # Build a dp array of how long supersequence would need to be if including a given char
    # Then back track from bottom right of row to find out what string is
    # Time O(n * m) where n and m are lengths of strings
    # Space O(n * m) where n and m are lengths of strings
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        dp = [
            [0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)
        ]

        # Initialize the base cases
        # When str2 is empty, the supersequence is str1 itself (length = row index)
        for row in range(str1_length + 1):
            dp[row][0] = row

        # When str1 is empty, the supersequence is str2 itself (length = col index)
        for col in range(str2_length + 1):
            dp[0][col] = col

        # Fill the DP table
        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    # If characters match, inherit the length from the diagonal +1
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # If characters do not match, take the minimum length option +1
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        super_sequence = []
        row, col = str1_length, str2_length

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                # If characters match, take it from diagonal
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                # If str1’s character is part of the supersequence, move up
                super_sequence.append(str1[row - 1])
                row -= 1
            else:
                # If str2’s character is part of the supersequence, move left
                super_sequence.append(str2[col - 1])
                col -= 1

        # Append any remaining characters
        # If there are leftover characters in str1
        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        # If there are leftover characters in str2
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        # Reverse the built sequence to get the correct order
        return "".join(super_sequence[::-1])

    # DP algorithm
    # Time O(n * m * (n+m)) where n and m are lengths of strings
    # Space O(n * (n+m)) where n and m are lengths of strings
    def shortestCommonSupersequence_slow_dp(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        # Initialize the first row (when str1 is empty, the supersequence is str2's prefix)
        prev_row = [str2[0:col] for col in range(str2_length + 1)]

        # Fill the DP table row by row
        for row in range(1, str1_length + 1):
            # Initialize the first column (when str2 is empty, the supersequence is str1's prefix)
            curr_row = [str1[0:row]] + [None for _ in range(str2_length)]

            for col in range(1, str2_length + 1):
                # If characters match, extend the supersequence from the diagonal value
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    # If characters do not match, choose the shorter supersequence
                    # From previous row (exclude current str1 char)
                    pick_s1 = prev_row[col]
                    # From previous column (exclude current str2 char)
                    pick_s2 = curr_row[col - 1]

                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )

            # Move to the next row (update previous row reference)
            prev_row = curr_row

        # Return the shortest common supersequence from the last cell
        return prev_row[str2_length]

    # Priority queue sorted by smallest string
    # Append character by character. Quit once we get a string with both strings empty
    # Exceeds time limit
    def shortestCommonSupersequence_pq(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        pq = []
        heappush(pq, SuperSequenceQueueItem("", 0, 0))

        while len(pq) > 0:
            item: SuperSequenceQueueItem = heappop(pq)

            # Check if this sequence is a complete subsequence
            if item.str1_index == len1 and item.str2_index == len2:
                return item.string_sequence
            
            # Append new entries to queue
            # Same character so append it and iterate both
            if item.str1_index < len1 and item.str2_index < len2 \
                 and str1[item.str1_index] == str2[item.str2_index]:
                next_str = item.string_sequence + str1[item.str1_index]
                heappush(pq, SuperSequenceQueueItem(next_str, item.str1_index + 1, item.str2_index + 1))
                continue

            # Append string of incrementing str1
            if item.str1_index < len1:
                next_str = item.string_sequence + str1[item.str1_index]
                heappush(pq, SuperSequenceQueueItem(next_str, item.str1_index + 1, item.str2_index))

            # Append string of incrementing str2
            if item.str2_index < len2:
                next_str = item.string_sequence + str2[item.str2_index]
                heappush(pq, SuperSequenceQueueItem(next_str, item.str1_index, item.str2_index + 1))
    
test_cases = [
    ["cabac", "abac", "cab"],
    ["dddbbdcaabccaccbababaacbdcbacddadcdacbdddcadccacdadbadcbabdaccbccdabcdcbcaccacbabdaccbdabba", "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb", "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa"],
    ["aaa", "aa", "aaa"]
]
solution = Solution()
for expected, str1, str2 in test_cases:
    actual = solution.shortestCommonSupersequence(str1, str2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}.")
        print(f"\tINPUTS: str1: {str1}, str2: {str2}")

print("Ran all tests")