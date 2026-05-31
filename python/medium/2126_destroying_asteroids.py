class Solution:
    # Just sort asteroids and go through them
    # Time O(nlogn)
    # Space O(n) for sort
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()

        for ast_mass in asteroids:
            if mass >= ast_mass:
                mass += ast_mass
            # Asteroid is too big for planet to get through
            else:
                return False

        # We got through all them
        return True

test_cases = [
    [True, 10, [3,9,19,5,21]],
    [False, 5, [4,9,23,4]]
]
solution = Solution()
for expected, mass, asteroids in test_cases:
    actual = solution.asteroidsDestroyed(mass, asteroids)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: mass: {mass}, asteroids: {asteroids}")

print("Ran all tests")
