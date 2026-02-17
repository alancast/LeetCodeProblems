class Solution:
    # Time O(logn)
    # Space O(1)
    def countOperations(self, num1: int, num2: int) -> int:
        # total number of subtraction operations
        operations = 0
        while num1 and num2:
            # each step of the Euclidean algorithm
            operations += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1

        return operations

    # Time O(logn)
    # Space O(1)
    def countOperations_simulation(self, num1: int, num2: int) -> int:
        operations=0
        while num1!=0 and num2!=0:
            if num1>=num2:
                num1=num1-num2
            elif num2>=num1:
                num2=num2-num1
            operations+=1

        return operations

test_cases = [
    [3, 2, 3],
    [1, 10, 10]
]
solution = Solution()
for expected, num1, num2 in test_cases:
    actual = solution.countOperations(num1, num2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: num1: {num1}, num2: {num2}")

print("Ran all tests")
