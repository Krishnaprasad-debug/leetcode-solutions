class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        count=0
        q=deque()
        vis=set()
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]!=0):
                    if((i,j) not in vis):
                        sum=grid[i][j]
                        q.append((i,j))
                        vis.add((i,j))
                        while q:
                            x,y=q.popleft()
                            for dr,dc in dir:
                                nr=dr+x
                                nc=dc+y
                                if(0<=nr<len(grid) and 0<=nc<len(grid[0])):
                                    if((nr,nc) not in vis and grid[nr][nc]!=0):
                                        sum+=grid[nr][nc]
                                        q.append((nr,nc))
                                        vis.add((nr,nc))
                        if(sum%k==0):
                            count+=1
        return count
