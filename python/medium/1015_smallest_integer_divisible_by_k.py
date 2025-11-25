class Solution:
    # Same logic as below but just run loop k times since we know that will either
    # Produce an answer or have an overlap in the set somewhere
    # Time O(k)
    # Space O(1)
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for length_N in range(1,k+1):
            remainder = (remainder*10+1) % k
            if remainder == 0:
                return length_N
        
        # Never found possible answer
        return -1

    # Only need to keep track of remainder, if remainder ever repeats -1
    # Time O(k)
    # Space O(k) for set of remainders
    def smallestRepunitDivByK_set(self, k: int) -> int:
        answer = 1
        remainder = 1
        remainders_set = set()

        while remainder %k != 0:
            remainder = ((remainder * 10) + 1) % k
            answer += 1

            if remainder in remainders_set:
                return -1
            else:
                remainders_set.add(remainder)

        return answer

test_cases = [
    [1, 1],
    [-1, 2],
    [3, 3]
]
solution = Solution()
for expected, k in test_cases:
    actual = solution.smallestRepunitDivByK(k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: k: {k}")

print("Ran all tests")