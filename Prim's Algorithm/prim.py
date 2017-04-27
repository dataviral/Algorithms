""" Finding the shortest path between any to pairs of vertices i.e. the minimum spanning tree (MST)"""

def prims(G):
    V = []
    E = []

    V.append(0)
    m = len(G)

    while True:

        v = set(V)
        x = []
        for i in v:
            j = G[i].index(min(set(G[i]) - set([x if G[i].index(x) not in v else 999 for x in G[i] ]) ))
            x = [i, j]

        E.append(x)
        print(E)
        V.append(i)

        if len(V) == len(G):
            break

    return E

G = [ [999, 1, 5, 2], [1, 999, 999, 999], [5, 999, 999, 3], [2, 999, 3, 999] ];
print(prims(G));
