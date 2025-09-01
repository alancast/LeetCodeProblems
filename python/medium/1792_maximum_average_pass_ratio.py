from heapq import heappop, heappush
from typing import List


class Solution:
    # A max heap of how much adding 1 passing student ups the grade
    # Iterate over that til out of extra students
    # Time O((c+s)logc) as we constantly push top max heap (log c) each time
    # Space O(c)
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Populate the max_heap of how much adding an extra passing student will help
        add_student_max_heap = []
        for passer, total in classes:
            # How much will adding a passing student up the average
            improvement = ((passer+1)/(total+1)) - (passer/total)
            heappush(add_student_max_heap, (-improvement, passer, total))

        # Add students that will pass until there are none left
        while extraStudents > 0:
            # Add one student to whatever class will improve it most and find new improvement
            _, passer, total = heappop(add_student_max_heap)
            improvement = ((passer+2)/(total+2)) - ((passer+1)/(total+1))
            heappush(add_student_max_heap, (-improvement, passer+1, total+1))

            # Decrement extra students count
            extraStudents -= 1

        # Get average now of what passing ration will be
        c = len(classes)
        answer = 0
        for _, passer, total in add_student_max_heap:
            answer += (passer/total)
        answer /= c

        return round(answer, 5)

test_cases = [
    [.78333, [[1,2],[3,5],[2,2]], 2],
    [.53485, [[2,4],[3,9],[4,5],[2,10]], 4]
]
solution = Solution()
for expected, classes, extra_students in test_cases:
    actual = solution.maxAverageRatio(classes, extra_students)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: classes: {classes}, extra_students: {extra_students}")

print("Ran all tests")