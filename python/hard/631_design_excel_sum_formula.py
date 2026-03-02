from collections import defaultdict


class Excel:
    table: dict
    h: int
    w: int
    formulae: dict
    dependents: dict

    def __init__(self, height: int, width: str):
        # Create the initial table with every value set to 0
        self.table = defaultdict(list)
        col_width = self._col_to_int(width)
        for row in range(1, height+1):
            self.table[row] = [0 for _ in range(col_width+1)]

        self.h = height
        self.w = self._col_to_int(width)
        self.formulae = {}
        self.dependents = defaultdict(set)

    # Returns column as int
    def _col_to_int(self, col: str) -> int:
        return ord(col) - ord('A')

    # Returns all the cells in the numbers range
    def _cells_in(self, numbers: list[str]):
        for num in numbers:
            # Multiple cells
            if ":" in num:
                # Assume format is always topleft:bottom right
                tl, br = num.split(":")
                # Get cols and rows and go over all them
                tl_col, tl_row = self._col_to_int(tl[0]), int(tl[1:])
                br_col, br_row = self._col_to_int(br[0]), int(br[1:])
                for row in range(tl_row, br_row + 1):
                    for col in range(tl_col, br_col + 1):
                        yield (row, col)
            # Single cell
            else:
                yield (int(num[1:]), self._col_to_int(num[0]))

    def _clear_deps(self, row: int, col_int: int) -> None:
        if (row, col_int) in self.formulae:
            for cell in self._cells_in(self.formulae[(row, col_int)]):
                self.dependents[cell].discard((row, col_int))

    def _register_deps(self, row: int, col_int: int, numbers: list[str]) -> None:
        for cell in self._cells_in(numbers):
            self.dependents[cell].add((row, col_int))

    def _propagate(self, row: int, col_int: int) -> None:
        for (dr, dc) in list(self.dependents.get((row, col_int), [])):
            if (dr, dc) in self.formulae:
                self.table[dr][dc] = sum(self._evaluate(self.formulae[(dr, dc)]))
                self._propagate(dr, dc)

    def set(self, row: int, column: str, val: int) -> None:
        col_int = self._col_to_int(column)
        self._clear_deps(row, col_int)
        if (row, col_int) in self.formulae:
            del self.formulae[(row, col_int)]
        self.table[row][col_int] = val
        self._propagate(row, col_int)

    def get(self, row: int, column: str) -> int:
        col_int = self._col_to_int(column)
        return self.table[row][col_int]

    # Gets all the cell values in the numbers list
    def _evaluate(self, numbers_form: list[str]) -> list[int]:
        values = []
        for num in numbers_form:
            # Multiple cells (assume always in form topleft:bottomright)
            if ":" in num:
                tl, br = num.split(":")
                tl_col, tl_row = self._col_to_int(tl[0]), int(tl[1:])
                br_col, br_row = self._col_to_int(br[0]), int(br[1:])
                for row in range(tl_row, br_row + 1):
                    for col in range(tl_col, br_col + 1):
                        cell = self.table[row][col]
                        values.append(cell)
            else:
                c, r = self._col_to_int(num[0]), int(num[1:])
                cell = self.table[r][c]
                values.append(cell)

        return values

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        col_int = self._col_to_int(column)
        self._clear_deps(row, col_int)
        self.formulae[(row, col_int)] = numbers
        self._register_deps(row, col_int, numbers)
        self.table[row][col_int] = sum(self._evaluate(numbers))
        self._propagate(row, col_int)
        return self.table[row][col_int]

# Below is the correct idea but fails because the sets are updated
# as they are being iterated over, which is a no go
class ExcelBroken:
    # What the values of the full sheet are
    _sheet_values: dict
    # Sum cell to what cells it represents
    _sum_to_rep: dict
    # A cell to what cells it sums to
    _cell_to_sum: dict

    def __init__(self, height: int, width: str):
        self._sheet_values = defaultdict(int)
        self._sum_to_rep = defaultdict(set[tuple])
        self._cell_to_sum = defaultdict(set[tuple])

    def set(self, row: int, column: str, val: int) -> None:
        # Find the delta
        delta = val - self._sheet_values[(row, column)]
        # Update the value
        self._sheet_values[(row, column)] = val

        # Update any cells that sum this value
        for up_row, up_col in self._cell_to_sum[(row, column)]:
            self.set(up_row, up_col, self._sheet_values[(up_row, up_col)] + delta)

        # If this was previously a sum cell, remove it
        for rep_row, rep_col in self._sum_to_rep[(row, column)]:
            # Remove this from the list of cells it represents
            self._cell_to_sum[(rep_row, rep_col)].remove((row, column))
        # Remove this from the sum cells list
        del self._sum_to_rep[(row, column)]

    def get(self, row: int, column: str) -> int:
        return self._sheet_values[(row, column)]

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        temp_sum = 0

        # Go over all things we are summing, update temp_sum and data structures
        for number in numbers:
            # Just one cell
            if ":" not in number:
                # Get row and col
                num_col = number[0]
                num_row = int(number[1:])

                # Add to sum
                temp_sum += self._sheet_values[(num_row, num_col)]

                # Update structures to care about this cell
                self._cell_to_sum[(num_row, num_col)].add((row, column))
                self._sum_to_rep[(row, column)].add((num_row, num_col))
                continue

            # Cell blocks
            # Find the start and end rows
            parts = number.split(":")
            parts.sort()
            start_col = parts[0][0]
            end_col = parts[1][0]
            row_one = int(parts[0][1:])
            row_two = int(parts[1][1:])
            row_low = min(row_one, row_two)
            row_high = max(row_one, row_two)
            # Go over all cells
            for up_row in range(row_low, row_high + 1):
                for col_num in range(ord(start_col), ord(end_col) + 1):
                    up_col = chr(col_num)
                    # Add to sum
                    temp_sum += self._sheet_values[(up_row, up_col)]

                    # Update structures to care about this cell
                    self._cell_to_sum[(up_row, up_col)].add((row, column))
                    self._sum_to_rep[(row, column)].add((up_row, up_col))

        self._sheet_values[(row, column)] = temp_sum
        return temp_sum


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
test = Excel(3, "C")
test.set(1, "A", 2)
test.sum(3, "C", ["A1", "A1:B2"])
test.set(2, "B", 2)
test.get(3, "C")
