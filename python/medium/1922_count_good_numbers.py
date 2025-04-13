class Solution:
    MOD = pow(10, 9) + 7

    # Time O(logn) as pow function is logn
    # Space O(1)
    def countGoodNumbers(self, n: int) -> int:
        self.validate_input(n)
        # even digits must be even (0,2,4,6,8) (5 choices)
        # odd digits must be prime (2,3,5,7) (4 choices)
        num_odd_digits = n//2
        num_even_digits = num_odd_digits + (n % 2)

        # Turns out the pow function exceeds the time limit with large numbers
        # So need to use an in house implementation that uses modulo
        even_options = self.faster_pow(5, num_even_digits)
        odd_options = self.faster_pow(4, num_odd_digits)
        return (even_options * odd_options) % self.MOD
    
    def faster_pow(self, base: int, pow: int) -> int:
        answer = 1
        while pow > 0:
            # Our last iteration, so set the answer
            if pow % 2 == 1:
                answer = answer * base % self.MOD
            base = base * base % self.MOD
            pow //= 2

        return answer
    
    def validate_input(self, n: int) -> None:
        if n < 1 or n > pow(10, 15):
            raise ValueError("n must be between 1 and 10^15")
    
test_cases = [
    [5, 1],
    [400, 4],
    [564908303, 50]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.countGoodNumbers(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")