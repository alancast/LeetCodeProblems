from typing import List

class Solution:
    # Dynamic programming
    # Time O(n) Space O(n)
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Work backwards. 
        # Create a list of the same size and populate it with 
        # the max value obtainable if you answer that question
        # Which can be computed by points + question[i + skipNum] if you take the question
        # or question[i+i] if you skip it. Whichever is greater
        num_questions = len(questions)
        points_attainable = [0] * (num_questions+1)
        for i in range(num_questions-1, -1, -1):
            value = questions[i][0]
            num_skip = questions[i][1]

            if_answered = value
            # we are able to answer this and another
            if (i + num_skip) < (num_questions-1):
                if_answered = value + points_attainable[i+num_skip+1]
            
            points_attainable[i] = max(points_attainable[i+1], if_answered)

        return points_attainable[0]
    
testCases = [
    [19, [[9,1], [3,1], [5,1], [10,1], [4,1]]],
    [7, [[7,1], [4,1]]],
    [7, [[7,3]]],
    [5, [[3,2], [4,3], [4,4], [2,5]]],
    [7, [[1,1], [2,2], [3,3], [4,4], [5,5]]],
    [5, [[1,5], [2,5], [3,5], [4,5], [5,5]]],
    [157, [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]]
]
solution = Solution()
for expected, questions in testCases:
    answer = solution.mostPoints(questions)
    if answer != expected:
        print(f"FAILED TEST! Expected {expected} but got {answer}. INPUTS: questions: {questions}")

print("Ran all tests")
