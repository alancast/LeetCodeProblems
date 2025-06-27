class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    # Return true if number is a palindrome in the given base (otherwise False)
    def isPalindrome(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    # This problem is garbage
    # Time O(n * L) where L is number of digits in largest palindrome used
    # Space O(1)
    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            # Generate odd digit palindromes
            for i in range(length, length * 10):
                if n <= 0:
                    break
                # Create base 10 palindrome
                p = self.createPalindrome(i, True)
                # See if it's a palindrome in base k as well
                # If so add to sum and make us need one less
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            # Generate even digit palindromes (bigger than odds before)
            for i in range(length, length * 10):
                if n <= 0:
                    break
                # Create base 10 palindrome
                p = self.createPalindrome(i, False)
                # See if it's a palindrome in base k as well
                # If so add to sum and make us need one less
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            
            # Add more digits to palindrome
            length *= 10

        return total
    
test_cases = [
    [25, 2, 5],
    [499, 3, 7],
    [20379000, 7, 17]
]
solution = Solution()
for expected, k, n in test_cases:
    actual = solution.kMirror(k, n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: k: {k}, n: {n}")

print("Ran all tests")