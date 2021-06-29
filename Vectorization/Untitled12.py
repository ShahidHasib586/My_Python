#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a = np.random.rand(5)


# In[3]:


print(a)


# In[4]:


print(a.shape)


# In[5]:


print(a.T)


# In[6]:


print(np.dot(a, a.T))


# In[7]:


a = a.reshape((5,1))


# In[8]:


a


# In[9]:


a.T


# In[10]:


print(np.dot(a, a.T))


# In[11]:


a = np.random.rand(5, 1)


# In[12]:


a.shape


# In[13]:


assert (a.shape == (5,1))


# In[14]:


a = np.random.rand(5)


# In[15]:


assert (a.shape == (5,1))


# In[ ]:




