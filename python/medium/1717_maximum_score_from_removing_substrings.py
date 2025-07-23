class Solution:
    # More space optimized and slightly more convoluted logic
    # Keep an a count and b count and reset when seeing a different char
    # Time O(n)
    # Space O(1)
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        a_count, b_count, total_points = 0, 0, 0

        # "ab" better than "ba" so look for that ordering
        if x >= y:
            # Go over all chars
            for i in range(n):
                # If it's an a add a count
                if s[i] == "a":
                    a_count += 1

                # If it's a b see if we can remove an "ab" or not
                elif s[i] == "b":
                    # Can remove an "ab" so do that and add points
                    if a_count > 0:
                        a_count -= 1
                        total_points += x
                    # Can't remove an "ab" but add b for potential future "ba"
                    else:
                        b_count += 1
                # Not an a or b, so make all possible "ba" pairs and reset counts
                else:
                    total_points += min(a_count, b_count) * y
                    # Reset counters for next segment
                    a_count = b_count = 0

            # Calculate points for any remaining "ba" pairs at the end
            total_points += min(a_count, b_count) * y

            return total_points

        # "ba" better than "ab" so look for that ordering        
        else:
            # Go over all the characters
            for i in range(n):
                # If it's a b add b count
                if s[i] == "b":
                    b_count += 1
                # If it's an a see if we can remove a "ba" or not
                elif s[i] == "a":
                    # Can remove a "ba" so do that and add points
                    if b_count > 0:
                        b_count -= 1
                        total_points += y
                    # Can't make a "ba" but could make "ab" in future
                    else:
                        a_count += 1
                # Not an a or b, so make all possible "ab" pairs and reset counts
                else:
                    # Calculate points for any remaining "ab" pairs
                    total_points += min(a_count, b_count) * x
                    # Reset counters for next segment
                    a_count = b_count = 0

            # Calculate points for any remaining "ab" pairs at the end
            total_points += min(a_count, b_count) * x

            return total_points

    # Manage with a stack and greedily pop higher value one
    # Time O(n) as we go over the string at most twice
    # Space O(n) as the whole string could go into the stack
    def maximumGain_space_not_concerned(self, s: str, x: int, y: int) -> int:
        score = 0
        high_priority_pair = "ab" if x > y else "ba"
        low_priority_pair = "ba" if high_priority_pair == "ab" else "ab"

        # First pass: remove high priority pair
        first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(first_pass)) // 2

        # Calculate score from first pass
        score += removed_pairs_count * max(x, y)

        # Second pass: remove low priority pair
        second_pass = self.remove_substring(first_pass, low_priority_pair)
        removed_pairs_count = (len(first_pass) - len(second_pass)) // 2

        # Calculate score from second pass
        score += removed_pairs_count * min(x, y)

        return score
    
    # Time O(n)
    # Space O(n)
    def remove_substring(self, s: str, target: str) -> str:
        char_stack = []

        # Iterate through each character in the input string
        for char in s:
            # See if current char completes target string from stack
            # If so remove previous char, otherwise add char to stack
            if char == target[1] and char_stack and char_stack[-1] == target[0]:
                char_stack.pop()
            else:
                char_stack.append(char)

        # Reconstruct the remaining string after removing target pairs
        return ''.join(char_stack)
    
test_cases = [
    [112374, "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha", 1926, 4320],
    [19, "cdbcbbaaabab", 4, 5],
    [20, "aabbaaxybbaabb", 5, 4]
]
solution = Solution()
for expected, s, x, y in test_cases:
    actual = solution.maximumGain(s, x, y)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, x: {x}, y: {y}")

print("Ran all tests")