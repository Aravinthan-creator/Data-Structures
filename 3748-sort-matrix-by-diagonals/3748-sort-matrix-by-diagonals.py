class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        temp = defaultdict(list)

        for i in range(n):
            for j in range(n):
                temp[n-i+j].append(grid[i][j])
        
        for k,val in temp.items():
            if k > n:
                val.sort()
            else:
                val.sort(reverse=True)
        
        for i in range(n):
            for j in range(n):
                grid[i][j] = temp[n-i+j].pop(0)
        
        return grid