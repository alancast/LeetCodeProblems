class Solution:
    # Just compute the angle of each hand and do the math
    # Time O(1)
    # Space O(1)
    def angleClock(self, hour: int, minutes: int) -> float:
        PER_HOUR = 30 # 360 / 12
        PER_MINUTE = 6 # 360 / 60

        # Compute hour angle from due north
        hour_angle = 0
        if hour < 12:  # noqa: PLR2004
            hour_angle += PER_HOUR * hour
        # Add minute effect
        hour_angle += ((minutes/60.0) * PER_HOUR)

        # Compute minute angle from due north
        minutes_angle = minutes * PER_MINUTE

        # Find angle between
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)

test_cases = [
    [165, 12, 30],
    [75, 3, 30],
    [76.5, 1, 57],
    [7.5, 3, 15]
]
solution = Solution()
for expected, hour, minutes in test_cases:
    actual = solution.angleClock(hour, minutes)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: hour: {hour}, minutes: {minutes}")

print("Ran all tests")
