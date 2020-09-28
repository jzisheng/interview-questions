class Solution:
    def spiralOrder(self, matrix):
        M = len(matrix) #nrows
        N = len(matrix[0]) #ncols
        
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        di = 0
        
        r,c = 0,0
        nr,nc = r+dr[di],c+dc[di]
        
        res = []
        visited = set()
        while len(res) <= M*N:
            res.append(matrix[r][c])
            visited.add((r,c))
            nr,nc = r+dr[di],c+dc[di]
            
            if 0 <= nr < M and 0 <= nc < N and (nr,nc) not in visited:
                r,c = nr,nc
            else:
                di = (di+1) % 4
                r,c = r+dr[di],c+dc[di]
        return res
    
    
    
arr = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    
s = Solution()
s.spiralOrder(arr)
