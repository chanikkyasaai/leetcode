class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        islandCount = 0

        def dfs(i,j):
            if i <0 or i>= m or j <0 or j >= n or (i,j) in visited or grid[i][j] == "0":
                return

            visited.add((i,j))

            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islandCount+=1

        return islandCount
                
        