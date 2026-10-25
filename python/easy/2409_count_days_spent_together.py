class Solution:
    # Just do the computation. Stupid problem
    # Time O(1)
    # Space O(1)
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days of month
        datesOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Prefix sum of how many days into year each month is
        prefixSum = [0]
        for date in datesOfMonths:
            prefixSum.append(prefixSum[-1] + date)

        # Compute days of all relevant dates
        arriveAliceDay = self.calculateDayOfYear(arriveAlice, prefixSum)
        leaveAliceDay = self.calculateDayOfYear(leaveAlice, prefixSum)
        arriveBobDay = self.calculateDayOfYear(arriveBob, prefixSum)
        leaveBobDay = self.calculateDayOfYear(leaveBob, prefixSum)

        # Do the math
        return max(
            0,
            min(leaveAliceDay, leaveBobDay)
            - max(arriveAliceDay, arriveBobDay)
            + 1,
        )

    # Compute day of year
    def calculateDayOfYear(self, day: str, prefixSum: list[int]) -> int:
        month = int(day[:2])
        date = int(day[3:])
        return prefixSum[month - 1] + date

test_cases = [
    [3, "08-15", "08-18", "08-16", "08-19"],
    [0, "10-01", "10-31", "11-01", "12-31"]
]
solution = Solution()
for expected, arrive_alice, leave_alice, arrive_bob, leave_bob in test_cases:
    actual = solution.countDaysTogether(arrive_alice, leave_alice, arrive_bob, leave_bob)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arrive_alice: {arrive_alice}, leave_alice: {leave_alice}, arrive_bob: {arrive_bob}, leave_bob: {leave_bob}")

print("Ran all tests")
