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
COUNT = 0

Vertices = {
    "0" : 0,
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0
}

adj_mat = {
    "0" : [0, 1, 0, 0, 0],
    "1" : [1, 0, 1, 1, 0],
    "2" : [0, 1, 0, 0, 0],
    "3" : [0, 1, 0, 0, 0],
    "4" : [1, 0, 0, 0, 0]
}

"""
    The Graph
    
            2
        /
0 - 1  - 3
 |
 4

 """

def DFS(start_vetex):
    dfs(start_vetex)
    for v in Vertices:
        if Vertices[v] == 0:
            dfs(v)

def dfs(v):
    # print()
    global COUNT
    COUNT +=1
    Vertices[v] = COUNT
    for w in Vertices:
        if Vertices[w] == 0 and adj_mat[v][int(w)] :
            dfs(w)

DFS("0")
print(Vertices)
