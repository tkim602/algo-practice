from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    reverse_graph[b].append(a)

S, T = map(int, input().split())


def bfs(start, graph, block=-1):
    visited = [False] * (n + 1)

    if block != -1:
        visited[block] = True

    visited[start] = True

    q = deque([start])

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if visited[nxt]:
                continue

            visited[nxt] = True
            q.append(nxt)

    return visited


# 1. S에서 출발해 갈 수 있는 곳
# 출근 중 T에 도착하면 끝이므로 T를 넘어가면 안 됨
from_S = bfs(S, graph, T)

# 2. T에서 출발해 갈 수 있는 곳
# 퇴근 중 S에 도착하면 끝
from_T = bfs(T, graph, S)

# 3. 어떤 정점에서 S로 갈 수 있는가?
# 원래 x -> S
# 역방향에서는 S -> x
to_S = bfs(S, reverse_graph)

# 4. 어떤 정점에서 T로 갈 수 있는가?
# 원래 x -> T
# 역방향에서는 T -> x
to_T = bfs(T, reverse_graph)


ans = 0

for i in range(1, n + 1):

    # 집과 회사는 제외
    if i == S or i == T:
        continue

    if from_S[i] and to_T[i] and from_T[i] and to_S[i]:
        ans += 1

print(ans)