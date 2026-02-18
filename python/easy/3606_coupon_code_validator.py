class Solution:
    # Just process each coupon one at a time then keep valid ones and sort
    # Time O(nlogn)
    # Space O(1) only need answer space
    def validateCoupons(
        self, code: list[str], businessLine: list[str], isActive: list[bool]
    ) -> list[str]:
        n = len(code)

        # Tuples of code, business line
        valid_coupons = []

        # Go over every coupon and see if valid, then sort
        for i in range(n):
            if not isActive[i]:
                continue

            if businessLine[i] not in (
                "electronics",
                "grocery",
                "pharmacy",
                "restaurant",
            ):
                continue

            # Validate code (empty code not allowed)
            temp_code = code[i]
            if not temp_code:
                continue
            temp_code = temp_code.replace('_', '')
            if temp_code and not temp_code.isalnum():
                    continue

            # If we got here it's a valid coupon
            valid_coupons.append((code[i], businessLine[i]))

        # Sort by businessLine then code
        valid_coupons.sort(key=lambda t: (t[1], t[0]))

        # Only take out the codes and then return answer
        return [c for c, _ in valid_coupons]

test_cases = [
    [
        ["PHARMA5", "SAVE20"],
        ["SAVE20", "", "PHARMA5", "SAVE@20"],
        ["restaurant", "grocery", "pharmacy", "restaurant"],
        [True, True, True, True],
    ],
    [
        ["ELECTRONICS_50"],
        ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
        ["grocery", "electronics", "invalid"],
        [False, True, True],
    ],
]


solution = Solution()
for expected, codes, business_lines, is_actives in test_cases:
    actual = solution.validateCoupons(codes, business_lines, is_actives)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(
            f"\tINPUTS: codes: {codes}, business_lines: {business_lines}, is_actives: {is_actives}"
        )

print("Ran all tests")
