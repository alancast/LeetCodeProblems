from typing import List


class Solution:
    # Just make last entry negative sum of first sequence
    # Time O(n)
    # Space O(1)
    def sumZero(self, n: int) -> List[int]:
        # n*(n+1)//2 is sum from 1-n
        # So can just do negative that num and 0 - (n-2)
        if n == 1:
            return [0]
        elif n == 2:
            return [-1, 1]
        
        answer = [i for i in range(n)]
        answer[-1] = ((-1)*(n-1)*(n-2))//2
        return answer
