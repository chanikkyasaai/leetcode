class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        islandCount = 0

        def bfs(i,j):
            visited.add((i,j))
            if 0 <= i-1 <= m-1 and 0<= j <= n-1 and grid[i-1][j] == "1" and (i-1,j) not in visited:
                bfs(i-1,j)
            if 0 <= i <= m-1 and 0<= j-1 <= n-1 and grid[i][j-1] == "1" and (i,j-1) not in visited:
                bfs(i,j-1)
            if 0 <= i+1 <= m-1 and 0<= j <= n-1 and grid[i+1][j] == "1" and (i+1,j) not in visited:
                bfs(i+1,j)
            if 0 <= i <= m-1 and 0<= j+1 <= n-1 and grid[i][j+1] == "1" and (i,j+1) not in visited:
                bfs(i,j+1)
            return
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                else:
                    if (i,j) in visited:
                        continue
                    bfs(i,j)
                    islandCount+=1

        return islandCount
                
        