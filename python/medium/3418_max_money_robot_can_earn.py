from collections import deque


class Solution:
    NEG_PLACEHOLDER = -1000000000

    # DP memoization search
    # Time O(mn)
    # Space O(n)
    def maximumAmount(self, coins: list[list[int]]) -> int:
        cols = len(coins[0])
        # Only need to store previous row
        dp = [[self.NEG_PLACEHOLDER] * 3 for _ in range(cols + 1)]

        dp[1] = [0] * 3
        for row in coins:
            for col, coin_value in enumerate(row):
                # Iterate neutralizations in descending order (from 2 to 1 to 0)
                # 2 neutralizations used
                # To right (this plus coin), from top (next plus coin),
                # ignore this to right (this -1 neutral), ignore this from top (next -1 neutral)
                dp[col + 1][2] = max(
                    dp[col][2] + coin_value, dp[col + 1][2] + coin_value, dp[col][1], dp[col + 1][1]
                )
                # 1 neutralization used
                # To right (this plus coin), from top (next plus coin),
                # ignore this to right (this -1 neutral), ignore this from top (next -1 neutral)
                dp[col + 1][1] = max(
                    dp[col][1] + coin_value, dp[col + 1][1] + coin_value, dp[col][0], dp[col + 1][0]
                )
                # No neutralizations used
                # Square to right will either be from left (so this plus coin) or from above (so next plus coin)
                dp[col + 1][0] = max(dp[col][0], dp[col + 1][0]) + coin_value

        return dp[cols][2]

    # THE BELOW IMPLEMENTATION IS THE RIGHT IDEA BUT IMPLEMENTED WRONG
    # IT DOES NOT WORK and opted not to spend time to fix
    # Example, if grid is just [[-4]] then it should return 0 but instead gets -4
    # Close to working though
    # Keep a queue of where to go and how many robbers been stopped
    # Time O(mn)
    # Space O(mn)
    def maximumAmount_idea_but_wrong(self, coins: list[list[int]]) -> int:  # noqa: PLR0912
        rows = len(coins)
        cols = len(coins[0])

        dp = [[[self.NEG_PLACEHOLDER for _ in range(3)] for _ in range(cols)] for _ in range(rows)]

        # Struct is total, row, col, num_robbers, stopped 1, stopped 2
        queue = deque([(coins[0][0], 0, 0, 0, 0, 0)])
        while queue:
            total, row, col, num_robbers, rob_1, rob_2 = queue.popleft()

            # This path won't be fruitful as we already have a better one
            if total < dp[row][col][num_robbers]:
                continue

            dp[row][col][num_robbers] = total

            # Append neighbors
            # To the right
            if col + 1 < cols:
                next_num = coins[row][col+1]
                if next_num >= 0:
                    queue.append((total + next_num, row, col + 1, num_robbers, rob_1, rob_2))
                # Figure out which robber to replace if any
                # Rob 1 is always less important than rob 2
                else:  # noqa: PLR5501
                    # Just skip this one
                    if num_robbers == 0:
                        queue.append((total, row, col + 1, 1, 0, next_num))
                    # Just add the second robber and move bigger theft to rob_2
                    elif num_robbers == 1:
                        queue.append((total, row, col + 1, 2, max(next_num, rob_2), min(next_num, rob_2)))
                    # Already 2 robbers so need to subtract one
                    else:  # noqa: PLR5501
                        # This robber is the one we care about least
                        if next_num >= rob_1:
                            queue.append((total + next_num, row, col + 1, num_robbers, rob_1, rob_2))
                        # Remove rob 1 and make this new rob_1
                        elif next_num >= rob_2:
                            queue.append((total + rob_1, row, col + 1, num_robbers, next_num, rob_2))
                        # Remove rob 1 but make this new rob 2
                        else:
                            queue.append((total + rob_1, row, col + 1, num_robbers, rob_2, next_num))

            # Down
            if row + 1 < rows:
                next_num = coins[row+1][col]
                if next_num >= 0:
                    queue.append((total + next_num, row + 1, col, num_robbers, rob_1, rob_2))
                # Figure out which robber to replace if any
                # Rob 1 is always less important than rob 2
                else:  # noqa: PLR5501
                    # Just skip this one
                    if num_robbers == 0:
                        queue.append((total, row + 1, col, 1, 0, next_num))
                    # Just add the second robber and move bigger theft to rob_2
                    elif num_robbers == 1:
                        queue.append((total, row + 1, col, 2, max(next_num, rob_2), min(next_num, rob_2)))
                    # Already 2 robbers so need to subtract one
                    else:  # noqa: PLR5501
                        # This robber is the one we care about least
                        if next_num >= rob_1:
                            queue.append((total + next_num, row + 1, col, num_robbers, rob_1, rob_2))
                        # Remove rob 1 and make this new rob_1
                        elif next_num >= rob_2:
                            queue.append((total + rob_1, row + 1, col, num_robbers, next_num, rob_2))
                        # Remove rob 1 but make this new rob 2
                        else:
                            queue.append((total + rob_1, row + 1, col, num_robbers, rob_2, next_num))

        return max(dp[rows-1][cols-1][0], dp[rows-1][cols-1][1], dp[rows-1][cols-1][2])

test_cases = [
    [8, [[0,1,-1],[1,-2,3],[2,-3,4]]],
    [40, [[10,10,10],[10,10,10]]]
]
solution = Solution()
for expected, coins in test_cases:
    actual = solution.maximumAmount(coins)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: coins: {coins}")

print("Ran all tests")
