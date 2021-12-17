#!/usr/bin/env python
# coding: utf-8

# In[1]:


graph = {
        'S' :['A' ,'B' ,[2 ,1]],
        'A' :['C', 'D', [2 ,3]],
        'B' :['D', 'E', [4 ,4]],
        'C' :['G', [4]],
        'D' :['G', [4]],
        'E' :['E', [0]],
        'G' :['G', [0]],
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
s = 'A'
g = 'G'
v = ucs(s, g)
j = 0
for i in v:
    print(v[j])
    j += 1


# In[ ]:




