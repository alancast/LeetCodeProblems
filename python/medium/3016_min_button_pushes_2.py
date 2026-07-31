from collections import Counter
from heapq import heapify, heappop


class Solution:
    # Count how many distinct letters there are
    # First 8 most common all have 1 button press
    # Next 8 all 2, then 3, then 4. Then do sum
    # Time O(n)
    # Space O(n)
    def minimumPushes(self, word: str) -> int:
        # Frequency map to store count of each letter
        frequency_map = Counter(word)

        # Priority queue to store frequencies in descending order
        # negative because default is min sort
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapify(frequency_queue)

        answer = 0
        index = 0
        # Calculate total number of presses (first 8 just 1, then 2, then 3)
        while frequency_queue:
            # # of presses required * # of times letter shows up
            answer += (1 + (index // 8)) * (-heappop(frequency_queue))
            index += 1

        return answer

test_cases = [
    [5, "abcde"],
    [12, "xyzxyzxyzxyz"],
    [24, "aabbccddeeffgghhiiiiii"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.minimumPushes(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")
