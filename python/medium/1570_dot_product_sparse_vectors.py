from typing import List


# Because we know it's sparse we can only care about the nonzeros
class SparseVector:
    # Time O(n) as we must go over all nums
    # Space O(L)
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n              

    # Time O(L)
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # Go over all non-zero elements in this Vector
        # If other vector is also non-zero at that index, update dot product
        for idx, value in self.nonzeros.items():
            if idx in vec.nonzeros:
                result += value * vec.nonzeros[idx]

        return result
