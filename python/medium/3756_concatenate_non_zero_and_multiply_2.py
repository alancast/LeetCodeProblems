class Solution:
    MOD = 10**9 + 7

    # Create prefix sums of sum and number
    # Then for each query do math on those
    # Time O(n + q)
    # Space O(n)
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        # Create prefix sums as well as numbers and lengths
        sums = [0]
        prefix_numbers = [0]
        prefix_lengths = [0]

        # Populate data structures
        running_sum = 0
        running_number = 0
        running_length = 0
        for char in s:
            if char != "0":
                digit = int(char)
                running_sum += digit
                running_number = (running_number * 10 + digit) % self.MOD
                running_length += 1

            sums.append(running_sum)
            prefix_numbers.append(running_number)
            prefix_lengths.append(running_length)

        # Store powers of 10 involved
        pow10 = [1] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            pow10[i] = (pow10[i - 1] * 10) % self.MOD

        # Process each query and get the answer
        answer = []
        for start, end in queries:
            sum_diff = sums[end + 1] - sums[start]
            length_diff = prefix_lengths[end + 1] - prefix_lengths[start]
            num_diff = (prefix_numbers[end + 1] - prefix_numbers[start] * pow10[length_diff]) % self.MOD
            answer.append((num_diff * sum_diff) % self.MOD)

        return answer

test_cases = [
    [[12340, 4, 9], "10203004", [[0,7],[1,3],[4,6]]],
    [[1, 0], "1000", [[0,3], [1,1]]],
    [[444444137], "9876543210", [[0,9]]]
]
solution = Solution()
for expected, s, queries in test_cases:
    actual = solution.sumAndMultiply(s, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, queries: {queries}")

large_s = "1" * 6000
big_mod = 0
for _ in range(6000):
    big_mod = (big_mod * 10 + 1) % solution.MOD
expected_large = [6000 * big_mod % solution.MOD]
actual_large = solution.sumAndMultiply(large_s, [[0, 5999]])
if expected_large != actual_large:
    print(f"FAILED LARGE TEST! Expected {expected_large} but got {actual_large}")

print("Ran all tests")
