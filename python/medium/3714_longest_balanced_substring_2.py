from collections import defaultdict


class Solution:
    # Go over string once for all the different combinations
    # Time O(n)
    # Space O(n)
    def longestBalanced(self, s: str) -> int:
        return max(
            self.mono(s),
            self.duo(s, 'a', 'b'),
            self.duo(s, 'a', 'c'),
            self.duo(s, 'b', 'c'),
            self.trio(s),
        )

    # Return the max length of a string of just one char
    # Time O(n)
    # Space O(1)
    def mono(self, s: str) -> int:
        if not s:
            return 0

        count = 1
        answer = 1
        # Go over string once and check each char to previous
        for i in range(1, len(s)):
            # If same longest balanced keeps growing
            if s[i] == s[i - 1]:
                count += 1
            # If different start new mono string
            else:
                count = 1

            # See if new max
            answer = max(answer, count)

        return answer

    # Return the max length of a string of just two chars
    # Time O(n)
    # Space O(n) as in theory all same string so pos dict is size of string
    def duo(self, s: str, c1: str, c2: str) -> int:
        # Dictionary of index when the delta was this
        delta_dict = {0: -1}
        answer = 0
        # Difference between occurrences of c1 and c2
        delta = 0

        # Go over all chars in string to see if longest duo string
        for i, ch in enumerate(s):
            # If we see the third char (we don't want)
            # Then this isn't right string so reset vals and go to next
            if ch not in (c1, c2):
                delta_dict.clear()
                delta_dict[0] = i
                delta = 0
                continue

            # Update difference in counts
            if ch == c1:
                delta += 1
            else:
                delta -= 1

            # See the first time the delta was this
            if delta in delta_dict:
                answer = max(answer, i - delta_dict[delta])
            else:
                delta_dict[delta] = i

        return answer

    # Return the max length of a string with all 3 chars
    # Time O(n)
    # Space O(n) as in theory deltas dict could be size of str
    def trio(self, s: str) -> int:
        cnt0 = cnt1 = cnt2 = 0
        # Dictionary of index when the tuple deltas were this
        # Key is b - a, c - a
        deltas_dict = {(0, 0): -1}
        answer = 0

        # Go over all chars in string to see if longest trio string
        for i, ch in enumerate(s):
            # Update counts
            if ch == 'a':
                cnt0 += 1
            elif ch == 'b':
                cnt1 += 1
            else:
                cnt2 += 1

            key = (cnt1 - cnt0, cnt2 - cnt0)

            # See if this deltas combo has already appeared in string
            if key in deltas_dict:
                answer = max(answer, i - deltas_dict[key])
            else:
                deltas_dict[key] = i

        return answer

    # Just enumerate all start and end positions
    # Time O(n^2)
    # Space O(1) as there are only 3 letters
    def longestBalanced_slow(self, s: str) -> int:
        n = len(s)
        answer = 0

        # Go over all start points
        for start in range(n):
            # See if we can break out early due to not beating answer
            if n - start <= answer:
                break

            # Reset counts dict
            counts = defaultdict(int)

            # Go over all endings until end and see if balanced
            for end in range(start, n):
                counts[s[end]] += 1

                # See if all chars have same count
                if len(set(counts.values())) == 1:
                    answer = max(answer, end - start + 1)

        return answer

test_cases = [
    [4, "abbac"],
    [3, "aabcc"],
    [2, "aba"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.longestBalanced(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
