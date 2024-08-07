import collections
def bfs(graph,root):
    queue=collections.deque([root])
    visited=set()
    while queue:
        vertex=queue.popleft()
        #once deqeue you are visiting that node
        visited.add(vertex)
        #finding all the adjacent nodes to vertex
        for i in graph[vertex]:
            if i not in visited:
            #while performing enqueue operation check if the node is not in visited 
                queue.append(i)
    return(visited)
    

graph={0:[1,2,3],1:[0,2],2:[0,4],3:[0],4:[2]}
print(bfs(graph,0))
