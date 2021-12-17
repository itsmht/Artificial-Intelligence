#!/usr/bin/env python
# coding: utf-8

# In[1]:


from queue import PriorityQueue
graph = {
    'S': ['A', 'B', 'C', [5, 2, 4]],
    'A': ['D', 'E', [9, 4]],
    'B': ['G', [4]],
    'C': ['F', [2]],
    'D': ['H', [7]],
    'E': ['G', [6]],
    'F': ['G', [1]],
    'G': ['G', [0]],
    'H': ['G', [0]],
}
route = []
visited = []
sortedWeight = []
sortedPoint = []
def ucs(start, destination):
    route.append(start)
    while len(route) > 0:
        vertex = route.pop(0)
        if vertex not in visited:
            visited.append(vertex)

            sortedWeight = sorted(graph[vertex][len(graph[vertex]) - 1])
            print(sortedWeight)
            for i in sortedWeight:
                sortedPoint.append(graph[vertex][graph[vertex][len(graph[vertex]) - 1].index(i)])
            route.extend(set(sortedPoint) - set(visited))
        if visited.__contains__(destination):
            break
    return visited
s = 'S'
g = 'G'
v = ucs(s, g)
j = 0
for i in v:
    print(v[j])
    j += 1


# In[ ]:




