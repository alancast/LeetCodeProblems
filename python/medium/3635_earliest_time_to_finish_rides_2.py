class Solution:
    # Try both orders, land -> water and water -> land
    # Just go through each of them linearly
    # Time O(n + m)
    # Space O(1)
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        # Just a number outside of range
        INF = 1000000

        # Find earliest finish time if doing 1 before 2
        def solve(start1: list[int], duration1: list[int], start2: list[int], duration2: list[int]) -> int:
            # Find earliest finish time of first one
            n = len(start1)
            finish1 = INF
            for i in range(n):
                finish1 = min(finish1, start1[i] + duration1[i])

            # Find earliest finish time of second one now
            m = len(start2)
            both_finish = INF
            for i in range(m):
                # Equation is earliest possible start time (max start/finish1) plus duration
                both_finish = min(both_finish, max(start2[i], finish1) + duration2[i])

            # Return lowest time
            return both_finish

        # Test both orders, land then water and water then land. See which is less
        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        # Return whichever is lower
        return min(land_water, water_land)

test_cases = [
    [9, [2,8], [4,1], [6], [3]],
    [14, [5], [3], [1], [10]]
]
solution = Solution()
for expected, land_start_time, land_duration, water_start_time, water_duration in test_cases:
    actual = solution.earliestFinishTime(land_start_time, land_duration, water_start_time, water_duration)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: land_start_time: {land_start_time}, land_duration: {land_duration}")
        print(f"\tINPUTS: water_start_time: {water_start_time}, water_duration: {water_duration}")

print("Ran all tests")
