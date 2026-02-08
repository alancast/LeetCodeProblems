def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    answer = 0

    # Loop over all string/number lengths
    for size in range(len(str(A)), len(str(B)) + 1):
        # Loop over all digits and see if the number is in the range
        for i in range(1, 10):
            num = int(str(i) * size)
            if A <= num <= B:
                answer += 1
            elif num > B:
                break

    return answer

test_cases = [
    [5, 75, 300],
    [9, 1, 9],
    [1, 9999999, 9999999]
]
for expected, A, B in test_cases:
    actual = getUniformIntegerCountInInterval(A, B)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: A: {A}, B: {B}")

print("Ran all tests")
