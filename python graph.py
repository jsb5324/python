#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


def f(x):
    return x*(x-2)


# In[8]:


print(f(np.array([0,2,-10,5])))


# In[9]:


x = np.linspace(-5,5,10)


# In[14]:


def f2(x):
    r = -2*x**3 + x**2+15*x
    return r

x = np.linspace(-3,3,100)
plt.plot(x,f2(x))
plt.show()

