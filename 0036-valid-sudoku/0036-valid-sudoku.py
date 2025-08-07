class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
    
        # Check all columns  
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        # Check all 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        if board[row][col] != '.':
                            if board[row][col] in seen:
                                return False
                            seen.add(board[row][col])
        return True