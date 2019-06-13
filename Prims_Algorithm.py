def prims(graph,src):
    """ calculates a shortest path tree routed in src to dest"""
    tree={}
    Q={}
    for v in graph:
        Q[v]= float('inf')
    weigth=0
    Q[src]=0
    while Q:
        u=min(Q, key=Q.get)
        weigth=weigth+ Q[u]
        tree.update({u:Q[u]})
        del Q[u]
        for neighbor in graph[u] :
            if neighbor in Q:
                if Q[neighbor] > graph[u][neighbor]:
                   Q[neighbor] = graph[u][neighbor]
    return (weigth, tree)
graph = {'s': {'a': 2, 'b': 1},
            'a': {'b': 4, 'c':8},
            'b': {'d': 2},
            'c': {'d': 7, 't': 4},
            'd': {'t': 5},
            't': {'c': 4 , 'd': 5}}
src='s'
dist,tree=prims(graph,src)
print('Prims MST: ',tree," weght=",dist)


#Result: Prims MST:  {'s': 0, 'b': 1, 'a': 2, 'd': 2, 't': 5, 'c': 3}  weght= 13
