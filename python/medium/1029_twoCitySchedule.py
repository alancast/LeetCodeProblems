from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by gain company gets by sending person to city A instead of city B
        costs.sort(key = lambda x : x[0] - x[1])
        
        total = 0
        n = len(costs) // 2
        # Send the first n people to the city A and the others to city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]

        return total

testCases = [
    [[[10,20],[30,200],[400,50],[30,20]], 110],
    [[[10,20],[30,200]], 50],
    [[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859],
    [[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], 3086]
]
implementation = Solution()
for costs, expected in testCases:
    answer = implementation.twoCitySchedCost(costs)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {costs}")