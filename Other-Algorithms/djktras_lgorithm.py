def dijkstra(graph,src,dest):
    """ calculates a shortest path tree routed in src to dest"""
   
    distances={}
    predecessors={}
    Q={}
  
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')    
    for v in graph:
        distances[v]= float('inf')
        predecessors[v]=None
        Q[v]= float('inf')
    
    distances[src]=0
    Q[src]=0
       
    while Q:
        u=min(Q, key=Q.get)
        
        del Q[u]
        
        for neighbor in graph[u] :
            
            if neighbor in Q:
                
                new_distance = distances[u] + graph[u][neighbor]
                if new_distance < distances.get(neighbor):
                    distances[neighbor] = new_distance
                    Q[neighbor] = new_distance
                    predecessors[neighbor] = u
    return (distances, predecessors)


graph = {'s': {'a': 2, 'b': 1},
            'a': {'b': 4, 'c':8},
            'b': {'d': 2},
            'c': {'d': 7, 't': 4},
            'd': {'t': 5},
            't': {'c': 3, 'd': 5}}
src='s'
dest='t' 
dist,prev=dijkstra(graph,src,dest)
    
path=[]
pred=dest
while pred != None:
        path.append(pred)
        pred=prev.get(pred,None)
print('shortest path: '+str(path)+" cost="+str(dist[dest]))
