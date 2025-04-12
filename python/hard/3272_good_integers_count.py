from math import factorial
from typing import List

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        """
        Counts the number of "good" integers of length `n` 
        where the number is divisible by `k` and can be rearranged into a palindrome.

        Args:
            n (int): The number of digits in the integer. Must be between 1 and 10.
            k (int): The divisor for the numbers. Must be between 1 and 9.

        Returns:
            int: The count of "good" integers satisfying the conditions.

        Raises:
            ValueError: If `n` is not between 1 and 10, or if `k` is not between 1 and 9.
        """
        self.validate_inputs(n, k)
        return self.count_good_integers(n, k)
    
    def count_good_integers(self, n: int, k: int) -> int:
        sorted_palindrome_numbers = set()
        # only care about first half of number since palindrome is same chars on other side
        lower_bound = pow(10, ((n-1)//2))
        is_odd_digits = n & 1

        # find all the palindromic numbers
        for i in range(lower_bound, lower_bound*10):
            num_str = str(i)
            num_str += num_str[::-1][is_odd_digits:]
            num = int(num_str)
            if num % k == 0:
                sorted_num_str = "".join(sorted(num_str))
                sorted_palindrome_numbers.add(sorted_num_str)

        # Now we have all the palindromic numbers
        # So compute the number of permutations they can create
        count_good_numbers = 0
        for num_str in sorted_palindrome_numbers:
            # Count of each integer, as if there are multiple of one then less perms
            digit_counts = [0] * 10
            for char in num_str:
                digit_counts[int(char)] += 1

            # Calculate permutations and combinations
            # remove all numbers that start with 0
            total = (n - digit_counts[0]) * factorial(n-1)
            # divide by each time a digit has multiple
            # If all digits are unique then these will all be 1 and it just equals n!
            for digit_count in digit_counts:
                total //= factorial(digit_count)
            count_good_numbers += total

        return count_good_numbers
    
    # This likely exceeds the time limit. 
    def countGoodIntegers_brute_force(self, n: int, k: int) -> int:
        lower_bound = pow(10, n-1)
        upper_bound = int('9' * n)
        added_numbers = set()
        count_good_nums = 0
        
        for num in range(lower_bound, upper_bound + 1):
            # not divisible so don't care if it's a palindrome
            if num % k != 0:
                continue
            if self.is_palindrome(num):
                # this is a palindrome, so gen all perms of the digits and add
                # But only if we haven't already genned perms for it
                if str(sorted(str(num))) in added_numbers:
                    continue
            
                permutations = self.get_permutations(str(num))
                for perm in permutations:
                    if perm[0] == '0':
                        continue
                    if perm not in added_numbers:
                        added_numbers.add(perm)
                        count_good_nums += 1
        
        return count_good_nums
    
    def is_palindrome(self, num: int) -> bool:
        num_str = str(num)
        for i in range((len(num_str)//2)+1):
            if num_str[i] != num_str[-(i+1)]:
                return False

        return True
    
    def get_permutations(self, num_str: str) -> List[str]:
        if len(num_str) <= 1:
            return [num_str]
        
        permutations = []
        for i, char in enumerate(num_str):
            remaining_chars = num_str[:i] + num_str[i+1:]
            sub_permutations = self.get_permutations(remaining_chars)
            for sub_permutation in sub_permutations:
                permutations.append(char + sub_permutation)
        
        return permutations
    
    def validate_inputs(self, n: int, k: int) -> None:
        if n < 1 or n > 10:
            raise ValueError("n must be between 1 and 10")
        if k < 1 or k > 9:
            raise ValueError("k must be between 1 and 9")

test_cases = [
    [27, 3, 5],
    [2, 1, 4],
    [2468, 5, 6]
]
solution = Solution()
for expected, n , k in test_cases:
    actual = solution.countGoodIntegers(n, k)
    if expected != actual:
        print(f"FAILED TEST: Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, k: {k}")

print("Ran all tests")