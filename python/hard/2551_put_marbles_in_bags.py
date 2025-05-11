from typing import List


class Solution:
    # All that matters is start and end of each bag
    # So all that matters is pairs next to each other
    # Compute all the pairs, then sort the pair sums
    # Answer then is sum(max k-1 pairs) - sum(min k-1 pairs)
    # Time O(nlogn) as we sort a list of size n-1
    # Space O(n) as we store full pairs of size n-1
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if n == k or k == 1:
            return 0
        
        pair_sums = [0] * (n - 1)
        for i in range(n-1):
            pair_sums[i] = weights[i] + weights[i+1]

        pair_sums.sort()

        # # find minimum k-1 pair weights
        # min_pair_weights = 0
        # for i in range(k-1):
        #     min_pair_weights += pair_sums[i]

        # # find maximum k-1 pair weights
        # max_pair_weights = 0
        # for i in range(n-2, n-k-1, -1):
        #     max_pair_weights += pair_sums[i]


        # return max_pair_weights - min_pair_weights

        # More efficient version of what's above
        answer = 0
        for i in range(k - 1):
            answer += pair_sums[n - 2 - i] - pair_sums[i]

        return answer
    
test_cases = [
    [4, [1,3,5,1], 2],
    [3, [1,4,2,5,2], 3],
    [0, [1,3], 2]
]
solution = Solution()
for expected, weights, k in test_cases:
    actual = solution.putMarbles(weights, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: weights: {weights}, k: {k}")

print("Ran all tests")