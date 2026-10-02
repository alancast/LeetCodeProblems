class Solution:
    # DP
    # Time O(n)
    # Space O(n)
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        #f(4,r) = min(f(3,r) + reg(3), f(3,e) + reg(3))
        #f(4,e) = min(f(3,r) + exp_cost + exp(3), f(3,e) + exp(3))
        n = len(regular)

        reg = 0
        exp = expressCost
        answer = [0] * n
        for i in range(n):
            reg_x = min(reg, exp) + regular[i]
            exp_x = min(reg + expressCost, exp) + express[i]
            reg, exp = reg_x, exp_x
            answer[i] = min(reg, exp)

        return answer

test_cases = [
    [[1,7,14,19], [1,6,9,5], [5,2,3,10], 8],
    [[10,15,24], [11,5,13], [7,10,6], 3]
]
solution = Solution()
for expected, regular, express, express_cost in test_cases:
    actual = solution.minimumCosts(regular, express, express_cost)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: regular: {regular}, express: {express}, expressCost: {express_cost}")

print("Ran all tests")
