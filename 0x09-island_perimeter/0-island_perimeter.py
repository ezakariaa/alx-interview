def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # If the cell is land
                # Check the top cell
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check the bottom cell
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check the left cell
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check the right cell
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter

