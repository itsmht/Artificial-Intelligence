#!/usr/bin/env python
# coding: utf-8

# In[1]:


def getInvCount(arr):
    inv_count = 0
    for i in range(0, 2):
        for j in range(i + 1, 3):

            # Value 0 is used for empty space
            if (arr[j][i] > 0 and arr[j][i] > arr[i][j]):
                inv_count += 1
    return inv_count



def isSolvable(puzzle):
    invCount = getInvCount(puzzle)


    return (invCount % 2 != 0)

    # Driver code


puzzle = [[7, 1, 2], [5, 0, 4], [8, 3, 6]]
if (isSolvable(puzzle)):
    print("Solvable")
else:
    print("Not Solvable")


# In[ ]:




