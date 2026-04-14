class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_grid = [set() for _ in range(9)]                                                 
        seen_col = [set() for _ in range(9)]
        
        for i, row in enumerate(board):
            seen_row = set()
            for j, col in enumerate(row):
                if col == '.': 
                    continue

                # Check duplicates in rows
                if col in seen_row:
                    return False
                seen_row.add(col)

                # Check duplicates in col
                if col in seen_col[j]:
                    return False
                seen_col[j].add(col)

                # Check duplicates in 3x3 grid
                grid_idx = ( i // 3 ) * 3 + (j // 3)
                if col in seen_grid[grid_idx]:
                    return False
                seen_grid[grid_idx].add(col)
        return True

            