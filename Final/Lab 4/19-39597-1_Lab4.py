#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Graph:
    def __init__(self, totalNodes, adjacencyList, color):
        self.totalNodes = totalNodes
        self.adjacencyList = adjacencyList
        self.color = color
        self.nodeSequence = [""]*totalNodes

    def isSafe(self, node, c):
        for i in range(len(self.adjacencyList[node])):
            if(self.color[self.adjacencyList[node][i]] == c):
                return False
        return True


    def graphColorUtil(self, node, colorLimit):
        if node == '':
            # check and color any uncolored node
            for key, value in self.color.items():
                if value == 0:
                    self.graphColorUtil(key, colorLimit)
            return True

        for c in range(1, colorLimit+1):
            if(self.isSafe(node, c) == True):
                self.color[node] = c
                nextNode = self.getNodeWithMRV(node, colorLimit)
                if(self.graphColorUtil(nextNode, colorLimit) == True):
                    return True
                else:
                    self.color[node] = 0

        return False


    def graphColoring(self, colorLimit):
        # pdb.set_trace()
        startNode = self.pickNode('')
        if(self.graphColorUtil(startNode, colorLimit) == True):
            return True
        else:
            print("Solution does not exists")
            return False

    def pickNode(self, initialNode):
        maxCount = 0
        selectedNode = ''

        if (initialNode == ''):
            for node, neighbourList in self.adjacencyList.items():
                if (len(neighbourList) > maxCount and self.color[node] == 0):
                    maxCount = len(neighbourList)
                    selectedNode = node

        else:
            for i in range(len(self.adjacencyList[initialNode])):
                childNode = self.adjacencyList[initialNode][i]
                if (self.color[childNode] == 0 and len(self.adjacencyList[childNode]) > maxCount):
                    maxCount = len(self.adjacencyList[childNode])
                    selectedNode = childNode

        return selectedNode


    def getNodeWithMRV(self, parentNode, colorLimit):
        selectedNode = ''

        for i in range(len(self.adjacencyList[parentNode])):
            childNode = self.adjacencyList[parentNode][i]
            countColor = 0
            for c in range(1, colorLimit+1):
                if(self.isSafe(childNode, c) == True):
                    countColor += 1
            if (countColor < 0):
                selectedNode = childNode

        return selectedNode

adjacencyList = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'T', 'NSW'],
        'T': ['V']
};

color = {
        'WA': 0,
        'NT': 0,
        'SA': 0,
        'Q': 0,
        'NSW': 0,
        'V': 0,
        'T': 0
    };

g = Graph(7, adjacencyList, color)
colorLimit = 3
g.graphColoring(colorLimit)

for node, color in g.color.items():
    print(node, Color(color).name)


# In[ ]:




