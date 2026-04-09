class Solution:
    MOD = 10**9 + 7

    # Continuation of stupid problem, just with bigger ranges for time limits
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        T = int(n**0.5)

        groups = [[] for _ in range(T)]
        for left, right, k, v in queries:
            if k < T:
                groups[k].append((left, right, v))
            else:
                for i in range(left, right + 1, k):
                    nums[i] = nums[i] * v % self.MOD

        dif = [1] * (n + T)
        for k in range(1, T):
            if not groups[k]:
                continue
            dif[:] = [1] * len(dif)
            for left, right, v in groups[k]:
                dif[left] = dif[left] * v % self.MOD
                R = ((right - left) // k + 1) * k + left
                dif[R] = dif[R] * pow(v, self.MOD - 2, self.MOD) % self.MOD

            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % self.MOD
            for i in range(n):
                nums[i] = nums[i] * dif[i] % self.MOD

        # Compute XOR
        answer = 0
        for x in nums:
            answer ^= x

        return answer

test_cases = [
    [4, [1,1,1], [[0,2,1,4]]],
    [31, [2,3,1,5,4], [[1,4,2,3], [0,2,1,2]]]
]
solution = Solution()
for expected, nums, queries in test_cases:
    actual = solution.xorAfterQueries(nums, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, queries: {queries}")

print("Ran all tests")
