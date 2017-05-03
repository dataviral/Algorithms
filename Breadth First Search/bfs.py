"""
BFS(G):
// G = <V,E>
mark each vetex in V with 0  as mark of being unvisited
count <- 0
for each vertex v in V do
    if v is marked with 0
        bfs(v)

bfs(v)
count <- count + 1
mark v with count
initialize a queue with v
while queue is not empty do
    for each vertex w in V adjacent to the front vertex in queue do
        if w in marked with 0
            count <- count + 1
            mark w with count
            add w to queue
    remove the front vertex from the queue
"""
