#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

graph = {

    'S': {'A': 2, 'B': 1, },
    'A': {'C': 2, 'D': 3},
    'B': {'D': 4, 'E': 4},
    'C': {'G': 4},
    'D': {'G': 4},
    'E': {},
    'G': {}
}


def bfs(graph, start):
    visited = []

    queue = [start]

    while queue:

        node = queue.pop(0)
        if node not in visited:

            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


print(bfs(graph, 'A'))


# In[ ]:




