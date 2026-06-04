"""Ten line sums (R-05 / INV-05)."""

from entity.constants import GRID_SIZE


def sum_lines(grid: list[list[int]]) -> list[int]:
    """Return sums of 4 rows, 4 cols, 2 diagonals (10 lines)."""
    sums: list[int] = []
    for row in grid:
        sums.append(sum(row))
    for col in range(GRID_SIZE):
        sums.append(sum(grid[row][col] for row in range(GRID_SIZE)))
    sums.append(sum(grid[i][i] for i in range(GRID_SIZE)))
    sums.append(sum(grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)))
    return sums
