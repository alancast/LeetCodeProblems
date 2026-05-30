# pyright: reportArgumentType=false, reportIndexIssue=false, reportOperatorIssue=false
from sortedcontainers import SortedList


class Solution:
    # Fenwick Tree and process results in reverse order
    # Time O(qlogq + qlogm)
    # Space O(M + q)
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        mx = 50000

        st = SortedList([0, mx])
        for q in queries:
            if q[0] == 1:
                st.add(q[1])

        bt = [0] * (mx + 1)

        def update(x: int, v: int) -> None:
            while x < len(bt):
                bt[x] = max(bt[x], v)
                x += x & -x

        def query(x: int) -> int:
            res = 0
            while x > 0:
                res = max(res, bt[x])
                x -= x & -x
            return res

        pre = 0
        for x in st:
            if x == 0:
                continue
            update(x, x - pre)
            pre = x

        # Process the queries
        answer = []
        for q in reversed(queries):
            if q[0] == 2:  # noqa: PLR2004
                x, sz = q[1], q[2]
                idx = st.bisect_left(x)
                pre_val = x if idx < len(st) and st[idx] == x else st[idx - 1]
                max_space = query(pre_val)
                max_space = max(max_space, x - pre_val)
                answer.append(max_space >= sz)
            else:
                x = q[1]
                idx = st.bisect_left(x)
                pre_val = st[idx - 1]
                nxt = st[idx + 1]
                update(nxt, nxt - pre_val)
                st.discard(x)

        # Reverse answer because we processed queries in reverse
        return answer[::-1]

test_cases = [
    [[False, True, True], [[1,2],[2,3,3],[2,3,1],[2,2,2]]],
    [[True, True, False], [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]]
]
solution = Solution()
for expected, queries in test_cases:
    actual = solution.getResults(queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: queries: {queries}")

print("Ran all tests")
