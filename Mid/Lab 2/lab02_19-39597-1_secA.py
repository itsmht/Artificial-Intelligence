#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
location=['A','B']
status=['Clean','Dirty']
table={('A','Clean'):'Right',
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left',
       ('B','Dirty'):'Suck',
       ('A','Clean','A','Clean'):'Right',
       ('A','Clean','A','Dirty'):'Suck',
       ('A','Clean','A','Clean','A','Clean'):'Right',
       ('A','Clean','A','Clean','A','Dirty'):'Suck'}
percepts=[]
def table_driven_agent(percept):
    percepts.append(percept)
    action=table.get(percept)
    print(action)
    return action
l=random.choice(location)
s=random.choice(status)
percpt=(l,s)
action=table_driven_agent(percpt)


# In[5]:


import random
location=['A','B']
status=['Clean','Dirty']
table={('A','Clean'):'Right',
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left',
       ('B','Dirty'):'Suck',
       (('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Dirty')):'Suck',
       (('A','Clean'),('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Clean'),('A','Dirty')):'Suck'}
percepts=[]
def table_driven_agent(percept):
    percepts.append(percept)
    action=table.get(percept)
    print(action)
    return action
for a in status:
    print(a)
l=random.choice(location)
s=random.choice(status)
percpt=(l,s)
action=table_driven_agent(percpt)


# In[6]:


import random
location=['A','B']
status=['Clean','Dirty']
table={('A','Clean'):'Right',
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left',
       ('B','Dirty'):'Suck',
       (('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Dirty')):'Suck',
       (('A','Clean'),('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Clean'),('A','Dirty')):'Suck'}
percepts=[]
def table_driven_agent(percept):
    percepts.append(percept)
    action=table.get(percept)
    print(action)
    return action
for a in status:
    print(a)
l=random.choice(location)
s=random.choice(status)
percpt=(l,s)
action=table_driven_agent(percpt)


# In[7]:


import random
location=['A','B']
status=['Clean','Dirty']
table={('A','Clean'):'Right',
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left',
       ('B','Dirty'):'Suck',
       (('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Dirty')):'Suck',
       (('A','Clean'),('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Clean'),('A','Dirty')):'Suck'}
percepts=[]
def table_driven_agent(percept):
    percepts.append(percept)
    action=table.get(percept)
    print(action)
    return action
for a in status:
    print(a)
l=random.choice(location)
s=random.choice(status)
percpt=(l,s)
action=table_driven_agent(percpt)


# In[8]:


import random
location=['A','B']
status=['Clean','Dirty']
table={('A','Clean'):'Right',
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left',
       ('B','Dirty'):'Suck',
       (('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Dirty')):'Suck',
       (('A','Clean'),('A','Clean'),('A','Clean')):'Right',
       (('A','Clean'),('A','Clean'),('A','Dirty')):'Suck'}
percepts=[]
def table_driven_agent(percept):
    percepts.append(percept)
    action=table.get(percept)
    #print('Agent percieved', percepts, 'And does', action)
    return action
def reflex_vaccum_agent(location,status):
    if(status== 'Dirty'):
        print('Agent percieved', location,status, 'And does', action)
    if(location=='A'):
        print('Agent percieved', location,status, 'And does', action)
    if(location=='B'):
        print('Agent percieved', location,status, 'And does', action)

for a in range(5):
    l = random.choice(location)
    s = random.choice(status)
    percpt = (l, s)
    action = table_driven_agent(percpt)
    reflex_vaccum_agent(l,s)


# In[ ]:




