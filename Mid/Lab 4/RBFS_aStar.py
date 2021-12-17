#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Queue:

    def __init__(self, pop_index=0):
        self.queue = []
        self.pop_index = pop_index

    def append(self, item):
        self.queue.append(item)

    def sortAppend(self, item, f):
        self.queue.append(item)
        self.queue.sort(key=f)

    def extend(self, items):
        self.queue.extend(items)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFOQueue is empty')

    def printQueue(self):
        print("Frontier Status After Adding .............")
        print([items.state for items in self.queue])

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item):
        return item in self.queue


graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Bucharest': {'Guirgiu': 90, 'Pitesti': 101, 'Urziceni': 85},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Drobeta': {'Craiova': 120, 'Mehadia': 75},
    'Eforie': {'Hirsova': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Droeta': 75, 'Lugoj': 70},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Sibiu': 151, 'Zerind': 70},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97},
    'Rimnicu Vilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Sibiu': {'Arad': 140, 'Oradia': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}


class graphProblem:

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, graphProblem):
        return [self.child_node(graphProblem, action)
                for action in graphProblem.actions(self.state)]

    def child_node(self, graphProblem, action):
        next_state = graphProblem.result(self.state, action)
        return Node(next_state, self, action,
                    graphProblem.path_cost(self.path_cost, self.state, action, next_state))

    def path(self):
        node, path_back = self, []

        while node:
            path_back.append(node)
            node = node.parent

        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]


def graph_search(problem, pop_index):
    node = Node(problem.initial)

    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)

    explored = set()

    frontier.append(node)

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        print("Parent: ", node.state,
              "Childs: ", [child.state for child in node.expand(problem)])

        explored.add(node.state)

        for child in node.expand(problem):
            if problem.goal_test(child.state): return child
            if child.state not in explored and child not in frontier: frontier.append(child)

    return None


gp = graphProblem("Arad", "Bucharest", graph)

heuristicSLD = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def best_first_search(problem, f, pop_index=0):
    node = Node(problem.initial)
    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)
    frontier.sortAppend(node, f)

    explored = Queue()

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        # print("Parent: ",node.state,
        #      "Childs: ",[child.state for child in node.expand(problem)])

        if problem.goal_test(node.state): return node
        explored.append(node)

        for child in node.expand(problem):
            if child not in explored and child not in frontier:
                frontier.sortAppend(child, f)

    return None


def uniform_cost_search(problem):
    return best_first_search(problem, lambda node: node.path_cost)


def GBFS(problem):
    return best_first_search(problem, lambda node: heuristicSLD[node.state])


def aStar_search(problem):
    return best_first_search(problem, lambda node: node.path_cost + heuristicSLD[node.state])


print("=======================================")
print()
print("----------GBFS State Space-------------")

goalNode = GBFS(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)
print("=======================================")
print()

print("----------A* State Space-------------")

goalNode = aStar_search(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)


# In[2]:


class Queue:

 

    def __init__(self,pop_index=0):
        self.queue = []
        self.pop_index=pop_index

 

    def append(self, item):
        self.queue.append(item)

 

    def sortAppend(self, item,f):
        self.queue.append(item)
        self.queue.sort(key=f)    

 

    def extend(self, items):
        self.queue.extend(items)     

 

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFOQueue is empty')

 

    def printQueue(self):
        print("Frontier Status After Adding .............")
        print([items.state for items in self.queue])

 

    def __len__(self):
        return len(self.queue)

 

    def __contains__(self, item):        
        return item in self.queue

 


graph={
    'S':{'A':2,'B':1,'G':9},
    'A':{'C':2,'D':3},
    'B':{'D':2,'E':4},
    'C':{'G':4},
    'D':{'G':4},
    'E':{},
    'G':{}
    }

 

 

class graphProblem:

 

    def __init__(self,initial,goal,graph):
        self.initial=initial
        self.goal=goal
        self.graph=graph

 

    def actions(self,state):
        return list(self.graph[state].keys())

 

    def result(self,state,action):
        return action

 

    def goal_test(self,state):
        return state == self.goal

 

    def path_cost(self,cost_so_far,state1,action,state2):
        return cost_so_far + self.graph[state1][state2]

 


class Node:
    def __init__(self,state,parent=None,action=None,path_cost=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost

 

    def expand(self,graphProblem):
        return [self.child_node(graphProblem,action)
                for action in graphProblem.actions(self.state)]
        

 

    def child_node(self,graphProblem,action):
        next_state=graphProblem.result(self.state,action)        
        return Node(next_state,self,action,
                    graphProblem.path_cost(self.path_cost,self.state,action,next_state))

 

    def path(self):        
        node, path_back = self, []       
        
        while node:            
            path_back.append(node)            
            node = node.parent
            
        
        return list(reversed(path_back))

 

    def solution(self):        
        return [node.action for node in self.path()[1:]]
    

 

def graph_search(problem,pop_index):    

 

    node=Node(problem.initial)
    
    if problem.goal_test(node.state): return node

 

    frontier = Queue(pop_index)
    
    explored = set()

 

    frontier.append(node)

 

    while frontier:

 

        frontier.printQueue()
        node = frontier.pop()

 

        print("Parent: ",node.state,
              "Childs: ",[child.state for child in node.expand(problem)])

 

        explored.add(node.state)

 

        for child in node.expand(problem):
            if problem.goal_test(child.state): return child
            if child.state not in explored and child not in frontier: frontier.append(child)

 

    return None

 

 

gp=graphProblem("S","G",graph)

 


heuristicSLD={
    'S':6,
    'A':0,
    'B':6,
    'C':4,
    'D':1,
    'E':10,
    'G':0  
    }

 


def best_first_search(problem,f,pop_index=0):
    
    node = Node(problem.initial)
    if problem.goal_test(node.state): return node
    
    frontier = Queue(pop_index)
    frontier.sortAppend(node,f)
    
    explored = Queue()
    
    while frontier:

 

        frontier.printQueue()
        node = frontier.pop()

 

        #print("Parent: ",node.state,
        #      "Childs: ",[child.state for child in node.expand(problem)])
        
        if problem.goal_test(node.state): return node
        explored.append(node)

 

        for child in node.expand(problem):
            if child not in explored and child not in frontier:
                frontier.sortAppend(child,f)

 

    return None

 


def uniform_cost_search(problem):
    return best_first_search(problem,lambda node:node.path_cost)

 


def GBFS(problem):
    return best_first_search(problem,lambda node:heuristicSLD[node.state])

 

def aStar_search(problem):
    return best_first_search(problem,lambda node:node.path_cost+heuristicSLD[node.state])
    

 

 

print("=======================================")
print()
print("----------GBFS State Space-------------")
      
goalNode=GBFS(gp)
print("Result:",goalNode.solution())
print("Path Cost: ", goalNode.path_cost)
print("=======================================")
print()

 

 

print("----------A* State Space-------------")
      
goalNode=aStar_search(gp)
print("Result:",goalNode.solution())
print("Path Cost: ", goalNode.path_cost)


# In[3]:


class Queue:

    def __init__(self, pop_index=0):
        self.queue = []
        self.pop_index = pop_index

    def append(self, item):
        self.queue.append(item)

    def sortAppend(self, item, f):
        self.queue.append(item)
        self.queue.sort(key=f)

    def extend(self, items):
        self.queue.extend(items)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFOQueue is empty')

    def printQueue(self):
        print("Frontier Status After Adding .............")
        print([items.state for items in self.queue])

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item):
        return item in self.queue


graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Bucharest': {'Guirgiu': 90, 'Pitesti': 101, 'Urziceni': 85},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Drobeta': {'Craiova': 120, 'Mehadia': 75},
    'Eforie': {'Hirsova': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Sibiu': 151, 'Zerind': 70},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97},
    'Rimnicu Vilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Sibiu': {'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}


class graphProblem:

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, graphProblem):
        return [self.child_node(graphProblem, action)
                for action in graphProblem.actions(self.state)]

    def child_node(self, graphProblem, action):
        next_state = graphProblem.result(self.state, action)
        return Node(next_state, self, action,
                    graphProblem.path_cost(self.path_cost, self.state, action, next_state))

    def path(self):
        node, path_back = self, []

        while node:
            path_back.append(node)
            node = node.parent

        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]


def graph_search(problem, pop_index):
    node = Node(problem.initial)

    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)

    explored = set()

    frontier.append(node)

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        print("Parent: ", node.state,
              "Childs: ", [child.state for child in node.expand(problem)])

        explored.add(node.state)

        for child in node.expand(problem):
            if problem.goal_test(child.state): return child
            if child.state not in explored and child not in frontier: frontier.append(child)

    return None


gp = graphProblem("Arad", "Bucharest", graph)

heuristicSLD = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def best_first_search(problem, f, pop_index=0):
    node = Node(problem.initial)
    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)
    frontier.sortAppend(node, f)

    explored = Queue()

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        # print("Parent: ",node.state,
        #      "Childs: ",[child.state for child in node.expand(problem)])

        if problem.goal_test(node.state): return node
        explored.append(node)

        for child in node.expand(problem):
            if child not in explored and child not in frontier:
                frontier.sortAppend(child, f)

    return None


def uniform_cost_search(problem):
    return best_first_search(problem, lambda node: node.path_cost)


def GBFS(problem):
    return best_first_search(problem, lambda node: heuristicSLD[node.state])


def aStar_search(problem):
    return best_first_search(problem, lambda node: node.path_cost + heuristicSLD[node.state])


print("=======================================")
print()
print("----------GBFS State Space-------------")

goalNode = GBFS(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)
print("=======================================")
print()

print("----------A* State Space-------------")

goalNode = aStar_search(gp)
print("Result:", goalNode.solution())
print("Path Cost: ", goalNode.path_cost)


# In[ ]:




