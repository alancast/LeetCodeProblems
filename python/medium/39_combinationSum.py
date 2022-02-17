from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedCandidates = sorted(candidates)
        candidatesSize = len(candidates)
        answer = []
        q = []
        for i in range(candidatesSize):
            num = sortedCandidates[i]
            if num > target:
                break
            q.append([[num], i, target - num])
        
        while q:
            entry, minIndex, newTarget = q.pop()
            if newTarget == 0:
                answer.append(entry)
                continue
            
            for i in range(minIndex, candidatesSize):
                tempEntry = entry.copy()
                num = sortedCandidates[i]
                if num > newTarget:
                    break
                tempEntry.append(num)
                q.append([tempEntry, i, newTarget - num])
        
        return answer

testCases = [
    [[2,3,6,7], 7, [[2,2,3],[7]]],
    [[2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]],
    [[2], 1, []],
    [[1], 1, [[1]]],
    [[1], 2, [[1,1]]]
]
solution = Solution()
for candidates, target, expected in testCases:
    answer = solution.combinationSum(candidates, target)
    sortedAnswer = sorted(answer)
    sortedExpected = sorted(expected)
    if sortedAnswer != sortedExpected:
        print(f"FAILED TEST: answer: {sortedAnswer}, expected {sortedExpected}. Inputs: {candidates}, {target}")