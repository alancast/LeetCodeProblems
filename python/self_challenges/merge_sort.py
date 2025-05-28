from typing import List


def merge_sort(nums: List[int]) -> None:
    _merge_sort(0, len(nums) - 1, nums)

def _merge_sort(l: int, r: int, nums: List[int]) -> None:
    if l >= r:
        return
    
    # To avoid overflow
    mid = l + ((r-l) // 2)

    _merge_sort(l, mid, nums)
    _merge_sort(mid+1, r, nums)
    _merge(l, mid + 1, r, nums)

def _merge(l: int, mid: int, r: int, nums: List[int]) -> None:
    temp_array = []

    starting_index = l
    right_index = mid
    while l < mid and right_index <= r:
        if nums[l] < nums[right_index]:
            temp_array.append(nums[l])
            l += 1
        else:
            temp_array.append(nums[right_index])
            right_index += 1

    # One list will still have items, so just append them all
    while l < mid:
        temp_array.append(nums[l])
        l += 1
    while right_index <= r:
        temp_array.append(nums[right_index])
        right_index += 1

    # Move them into the original array
    temp_index = 0
    for i in range(starting_index, r + 1):
        nums[i] = temp_array[temp_index]
        temp_index += 1

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