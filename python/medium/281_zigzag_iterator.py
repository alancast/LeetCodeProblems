class ZigzagIterator:
    v1: list[int]
    v1_len: int
    v1_idx: int
    v2: list[int]
    v2_len: int
    v2_idx: int
    v1_turn: bool

    def __init__(self, v1: list[int], v2: list[int]):
        self.v1 = v1
        self.v1_len = len(v1)
        self.v1_idx = 0
        self.v2 = v2
        self.v2_len = len(v2)
        self.v2_idx = 0

        # Make sure there is something in v1
        self.v1_turn = self.v1_len != 0

    # Time O(1)
    def next(self) -> int:
        # This should never happen but there for posterity sake (could throw)
        if not self.hasNext():
            return -1

        # V1 turn to return
        if self.v1_turn:
            answer = self.v1[self.v1_idx]
            self.v1_idx += 1

            # Make sure things are left in v2 before switching turns
            if self.v2_idx < self.v2_len:
                self.v1_turn = False

            return answer

        # V2 turn to return
        answer = self.v2[self.v2_idx]
        self.v2_idx += 1

        # Make sure things are left in v1 before switching turns
        if self.v1_idx < self.v1_len:
            self.v1_turn = True

        return answer

    # Time O(1)
    def hasNext(self) -> bool:
        return self.v1_idx < self.v1_len or self.v2_idx < self.v2_len

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
