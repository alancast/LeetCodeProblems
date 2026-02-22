from collections import Counter


class Solution:
    # Go over the string and count each character
    # Then put one in each bucket and make sure the buckets are long enough
    # Time O(n)
    # Space O(alphabet)
    def rearrangeString(self, s: str, k: int) -> str:
        counter = Counter(s)
        items = sorted([(freq, ch) for ch,freq in counter.items()])
        max_freq = items[-1][0]
        # Store a string for each bucket then concat them all together
        buckets = ["" for _ in range(max_freq)]

        bucket = 0
        # Go over all the items and put them in the bucket
        while items:
            freq, ch = items.pop()
            # If max frequency one goes in each bucket
            if freq == max_freq:
                for i in range(max_freq):
                    buckets[i] = buckets[i] + ch
                continue

            # Add this char to each bucket (in order of filling buckets first)
            while freq:
                bucket = bucket % (max_freq-1)
                buckets[bucket] = buckets[bucket] + ch
                freq -= 1
                bucket += 1

        # Go over all the buckets, if any of them are less than k then not possible
        for i in range(max_freq - 1):
            if len(buckets[i]) < k:
                return ""

        # If it is possible just join the buckets
        return "".join(buckets)

test_cases = [
    ["cbacba", "aabbcc", 3],
    ["", "aaabc", 3],
    ["acbdacba", "aaadbbcc", 2]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.rearrangeString(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")
