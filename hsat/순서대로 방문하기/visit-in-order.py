n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# nxn에서 m개 지점을 순서대로 방문; 상하좌우 중 인접; 벽 x; 한번 지나간 곳 다시 x
# 서로 다른 가지수 구하기 

order = [[-1]*n for _ in range(n)]

for i, (r,c) in enumerate(points):
    order[r][c] = i

# print(order)
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
ans = 0

visited = [[False]*n for _ in range(n)]

def dfs(r, c, idx):
    global ans

    if idx == m:
        ans += 1
        return
    
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if not (0 <= nr < n and 0 <= nc < n):
            continue
        
        if grid[nr][nc] == 1:
            continue
        
        if order[nr][nc] != -1 and order[nr][nc] != idx:
            continue

        if visited[nr][nc]:
            continue 
        
        visited[nr][nc] = True

        if order[nr][nc] == idx:
            dfs(nr, nc, idx+1)
        
        else:
            dfs(nr, nc, idx)
        
        visited[nr][nc] = False
    

sr, sc = points[0]
visited[sr][sc] = True
dfs(sr, sc, 1)

print(ans)




