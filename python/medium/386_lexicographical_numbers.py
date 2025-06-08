from typing import List


class Solution:
    # Time O(n) as each number has constant operations
    # Space O(1) as nothing other than answer list
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        current_number = 1

        # Generate numbers from 1 to n
        for _ in range(n):
            lexicographical_numbers.append(current_number)

            # If multiplying the current number by 10 is within the limit, do it
            if current_number * 10 <= n:
                current_number *= 10
            else:
                # Adjust the current number by moving up one digit
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10
                current_number += 1

        return lexicographical_numbers
    
test_cases = [
    [[1,10,11,12,13,2,3,4,5,6,7,8,9], 13],
    [[1,2], 2]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.lexicalOrder(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")