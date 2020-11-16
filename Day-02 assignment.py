#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ans:01

a=[]   #empty list
for i in range(0,10):
    b=int(input("Input:"))
    if(b%2==0):
        a.append(b)
print(a)


# In[12]:


#Ans:02

[{'a': i, 'b': 2*i} for i in range(5)]

In the above example, we can see how list comprehension can be used.
# In[5]:


#Ans:03

a=int(input("Input:"))
d={}
for i in range(1,a+1):
    d.update({i:i*i})
print(d)


# In[9]:


#Ans:04

import numpy as np
dist = {
    "x": 0, 
    "y": 0
}
z=int(input())
c=0
while (c!=z):
    n = input()
    c=c+1
    if not n:
        break

    direction,steps=n.split()
    if direction == "UP":
        dist["y"] += int(steps)
    elif direction == "DOWN":
        dist["y"] -= int(steps)
    elif direction == "LEFT":
        dist["x"] -= int(steps)
    elif direction == "RIGHT":
        dist["x"] += int(steps)
print (int(round((dist["x"]**2 + dist["y"]**2)**0.5)))


# In[ ]:




