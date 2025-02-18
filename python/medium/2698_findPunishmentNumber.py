from typing import List

class Solution:
    # Time O(nk) where k is time to find if partion-able
    # Space O(1)
    def punishmentNumber(self, n: int) -> int:
        return self.punishmentNumberIntMemoization(n)
    
    # Time O(nk) where k is time to find if partion-able which is 2^logn
    # Space O(logn)
    def punishmentNumberIntMemoization(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.__can_partition_int(square, current_num):
                punishment_num += square

        return punishment_num
    
    def __can_partition_int(self, remaining_num: int, target: int) -> bool:
        # Found a working partition
        if remaining_num == target:
            return True
        
        # Already too large, no sense in recursing further
        if target < 0 or remaining_num < target:
            return False
        
        # Recursively check all partitions for a valid partition
        # Because we know n <= 1000 we can hardcode these values because anything % 10k is already over target
        return (
            self.__can_partition_int(remaining_num // 10, target - remaining_num % 10)
            or self.__can_partition_int(remaining_num // 100, target - remaining_num % 100)
            or self.__can_partition_int(remaining_num // 1000, target - remaining_num % 1000)
        )

    # Time O(nk) where k is time to find if partion-able which is 2^logn
    # Space O(logn)
    def punishmentNumberStringMemoization(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square = current_num * current_num
            string_num = str(square)

            # Check if valid partition can be found and add squared number if so
            if self.__can_partition(string_num, current_num):
                punishment_num += square

        return punishment_num
    
    def __can_partition(self, string_num: str, target: int) -> bool:
        # Got to end of partition, see if we hit target num
        if len(string_num) == 0:
            return target == 0
        
        # Already too large, no sense in recursing further
        if target < 0:
            return False
        
        # Recursively check all partitions for a valid partition
        for index in range(len(string_num)):
            left = string_num[: index + 1]
            right = string_num[index + 1 :]
            left_num = int(left)

            if self.__can_partition(right, target - left_num):
                return True

        return False
    
    # Time O(nk) where k is time to find if partion-able which is 2^logn
    # Space O(nlogn + logn)
    def punishmentNumberMemoization(self, n: int) -> int:
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square = current_num * current_num
            string_num = str(square)

            # Initialize values in memoization array
            memo_array = [
                [-1] * (current_num + 1) for _ in range(len(string_num))
            ]

            # Check if valid partition can be found and add squared number if so
            if self.__find_partitions_basic(0, 0, string_num, current_num, memo_array):
                punishment_num += square

        return punishment_num
    
    def __find_partitions_basic(
        self, start_index, current_sum, string_num, target, memo
    ):
        # Check if partition is valid
        if start_index == len(string_num):
            return current_sum == target

        # Invalid partition found, so we return False
        if current_sum > target:
            return False

        # If the result for this state is already calculated, return it
        if memo[start_index][current_sum] != -1:
            return memo[start_index][current_sum] == 1

        partition_found = False

        # Iterate through all possible substrings starting with start_index
        for current_index in range(start_index, len(string_num)):
            # Create partition
            current_string = string_num[start_index : current_index + 1]
            addend = int(current_string)

            # Recursively check if valid partition can be found
            partition_found = partition_found or self.__find_partitions_basic(
                current_index + 1,
                current_sum + addend,
                string_num,
                target,
                memo,
            )
            if partition_found:
                memo[start_index][current_sum] = 1
                return True

        # Memoize the result for future reference and return its result
        memo[start_index][current_sum] = 0
        return False
    
testCases = [
    [10, 182],
    [1, 1],
    [6, 1],
    [37, 1478]
]
solution = Solution()
for n, expected in testCases:
    answer = solution.punishmentNumber(n)
    if answer != expected:
        print(f"FAILED TEST! Expected {expected} but got {answer}. INPUTS: {n}")

print("Ran all tests")