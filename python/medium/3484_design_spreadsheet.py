from collections import defaultdict


class Spreadsheet:
    # Map of cell str to value
    cell_map: defaultdict

    def __init__(self, rows: int):
        self.cell_map = defaultdict(int)

    # Time O(1)
    def setCell(self, cell: str, value: int) -> None:
        self.cell_map[cell] = value

    # Time O(1)
    def resetCell(self, cell: str) -> None:
        if cell not in self.cell_map:
            return

        del self.cell_map[cell]

    # Time O(n)
    def getValue(self, formula: str) -> int:
        # Get rid of equal sign
        formula = formula[1:]
        for i in range(len(formula)):
            cells = formula.split('+')
            # Get left (make sure it's a cell)
            left = 0
            if cells[0][0].isupper():
                left = self.cell_map[cells[0]]
            else:
                left = int(cells[0])

            # Get left (make sure it's a cell)
            right = 0
            if cells[1][0].isupper():
                right = self.cell_map[cells[1]]
            else:
                right = int(cells[1])
            
            return left + right

        return 0


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)