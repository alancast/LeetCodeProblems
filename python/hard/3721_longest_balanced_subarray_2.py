from collections import defaultdict, deque


class LazyTag:
    def __init__(self):
        self.to_add = 0

    def add(self, other):
        self.to_add += other.to_add
        return self

    def has_tag(self):
        return self.to_add != 0

    def clear(self):
        self.to_add = 0


class SegmentTreeNode:
    def __init__(self):
        self.min_value = 0
        self.max_value = 0
        self.lazy_tag = LazyTag()


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
        self._build(data, 1, self.n, 1)

    def add(self, left, r, val):
        tag = LazyTag()
        tag.to_add = val
        self._update(left, r, tag, 1, self.n, 1)

    def find_last(self, start, val):
        if start > self.n:
            return -1
        return self._find(start, self.n, val, 1, self.n, 1)

    def _apply_tag(self, i, tag):
        self.tree[i].min_value += tag.to_add
        self.tree[i].max_value += tag.to_add
        self.tree[i].lazy_tag.add(tag)

    def _push_down(self, i):
        if self.tree[i].lazy_tag.has_tag():
            tag = LazyTag()
            tag.to_add = self.tree[i].lazy_tag.to_add
            self._apply_tag(i << 1, tag)
            self._apply_tag((i << 1) | 1, tag)
            self.tree[i].lazy_tag.clear()

    def _pushup(self, i):
        self.tree[i].min_value = min(
            self.tree[i << 1].min_value, self.tree[(i << 1) | 1].min_value
        )
        self.tree[i].max_value = max(
            self.tree[i << 1].max_value, self.tree[(i << 1) | 1].max_value
        )

    def _build(self, data, left, r, i):
        if left == r:
            self.tree[i].min_value = data[left - 1]
            self.tree[i].max_value = data[left - 1]
            return

        mid = left + ((r - left) >> 1)
        self._build(data, left, mid, i << 1)
        self._build(data, mid + 1, r, (i << 1) | 1)
        self._pushup(i)

    def _update(self, target_l, target_r, tag, left, r, i):  # noqa: PLR0913
        if target_l <= left and r <= target_r:
            self._apply_tag(i, tag)
            return

        self._push_down(i)
        mid = left + ((r - left) >> 1)
        if target_l <= mid:
            self._update(target_l, target_r, tag, left, mid, i << 1)
        if target_r > mid:
            self._update(target_l, target_r, tag, mid + 1, r, (i << 1) | 1)
        self._pushup(i)

    def _find(self, target_l, target_r, val, left, r, i):  # noqa: PLR0913
        if self.tree[i].min_value > val or self.tree[i].max_value < val:
            return -1

        if left == r:
            return left

        self._push_down(i)
        mid = left + ((r - left) >> 1)

        if target_r >= mid + 1:
            res = self._find(target_l, target_r, val, mid + 1, r, (i << 1) | 1)
            if res != -1:
                return res

        if left <= target_r and mid >= target_l:
            return self._find(target_l, target_r, val, left, mid, i << 1)

        return -1


class Solution:
    # Prefix sum where even is +1 and odd is -1 so see when 0
    # Also create segment tree to see if things are distinct
    # Time O(nlogn)
    # Space O(n)
    def longestBalanced(self, nums: list[int]) -> int:
        occurrences = defaultdict(deque)

        def even_or_odd(x):
            return 1 if x % 2 == 0 else -1

        length = 0
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = even_or_odd(nums[0])
        occurrences[nums[0]].append(1)

        # Go over all nums and compute prefix sum
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1]

            # Check to see if this number is distinct
            occ = occurrences[nums[i]]
            if not occ:
                prefix_sum[i] += even_or_odd(nums[i])

            occ.append(i + 1)

        # Find the longest balanced subarray
        seg = SegmentTree(prefix_sum)
        for i in range(len(nums)):
            length = max(length, seg.find_last(i + length, 0) - i)
            next_pos = len(nums) + 1
            occurrences[nums[i]].popleft()
            if occurrences[nums[i]]:
                next_pos = occurrences[nums[i]][0]

            seg.add(i + 1, next_pos - 1, -even_or_odd(nums[i]))

        return length

test_cases = [
    [4, [2,5,4,3]],
    [5, [3,2,2,5,4]],
    [3, [1,2,3,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.longestBalanced(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
