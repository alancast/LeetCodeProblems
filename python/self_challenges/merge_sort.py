def merge_sort(nums: list[int]) -> None:
    _merge_sort(0, len(nums) - 1, nums)

def _merge_sort(left: int, right: int, nums: list[int]) -> None:
    if left >= right:
        return

    # To avoid overflow
    mid = left + ((right-left) // 2)

    _merge_sort(left, mid, nums)
    _merge_sort(mid+1, right, nums)
    _merge(left, mid + 1, right, nums)

def _merge(left: int, mid: int, right: int, nums: list[int]) -> None:
    temp_array = []

    starting_index = left
    right_index = mid
    while left < mid and right_index <= right:
        if nums[left] < nums[right_index]:
            temp_array.append(nums[left])
            left += 1
        else:
            temp_array.append(nums[right_index])
            right_index += 1

    # One list will still have items, so just append them all
    while left < mid:
        temp_array.append(nums[left])
        left += 1
    while right_index <= right:
        temp_array.append(nums[right_index])
        right_index += 1

    # Move them into the original array
    for temp_index, value in enumerate(temp_array):
        nums[starting_index + temp_index] = value

test_cases = [
    [[1,2,3,4,5], [5,4,3,2,1]],
    [[], []],
    [[1,2,3,4,5], [1,2,4,3,5]],
    [[1,2,3,4,5], [1,2,3,4,5]],
    [[1], [1]],
    [[1,2], [2,1]]
]
for expected, nums in test_cases:
    actual = nums.copy()
    merge_sort(actual)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
