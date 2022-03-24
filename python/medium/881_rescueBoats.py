from typing import List


class Solution:
    # O(nlogn) time (for sort). O(n) space because of sort
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        lightest = 0
        heaviest = len(people) - 1
        ans = 0

        # Try to pair the lightest and heaviest if not possible heaviest goes alone
        while lightest <= heaviest:
            ans += 1
            if people[lightest] + people[heaviest] <= limit:
                lightest += 1
            heaviest -= 1

        return ans

testCases = [
    [[1,2], 3, 1],
    [[1,1,1,2,2,2], 3, 3],
    [[1,3,2], 3, 2],
    [[3,2,2,1], 3, 3],
    [[4,4,4,4,3], 5, 5],
    [[4,4,4,4,4], 5, 5],
    [[3,5,3,4], 5, 4]
]
implementation = Solution()
for people, limit, expected in testCases:
    answer = implementation.numRescueBoats(people, limit)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: people: {people} limit: {limit}")