class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mat=[[0]*len(grid[0]) for i in range(len(grid))]
        mat[0][0]=grid[0][0]
        for i in range(1,len(mat)):
            mat[i][0]=mat[i-1][0]+grid[i][0]
        for j in range(1,len(mat[0])):
            mat[0][j]=mat[0][j-1]+grid[0][j]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                mat[i][j]=min(mat[i-1][j],mat[i][j-1])+grid[i][j]
        return mat[-1][-1]