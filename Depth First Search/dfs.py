"""
DFS(G):
// G = <V,E>
mark each vertex in V with 0  as the mark of being unvisited
count <- 0
for each vertex v in V do
    if v is marked with 0
        dfs(v)

dfs(v):
count <- count + 1
mark v with count
for each vertex w in V adjacent to w do
    if w is marked with 0
        dfs(w)
"""
