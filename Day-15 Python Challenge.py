#!/usr/bin/env python
# coding: utf-8

# # Day-15 Python Challenge

# # Pandas Part - 2

# In[41]:


import pandas as pd


# In[42]:


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.head()


# # Type Function

# In[43]:


df['Name'][0:10]


# In[44]:


a = df['Name'][0:10]


# In[45]:


type(a)


# # Series function

# In[46]:


b = ['Pal', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']


# In[47]:


pd.Series(a, index = b)


# # Create Data Frame 

# In[61]:


a1 = pd.Series([200,300,400,500,600], index = [2,3,4,5,6])


# In[62]:


a1


# In[63]:


a2 = pd.Series([700,800,900,1000], index = [7,8,9,10])


# In[68]:


a2


# In[65]:


a3 = pd.concat([a1, a2])


# In[66]:


a3


# In[70]:


a1*a2


# In[71]:


df.head()


# # Delete Column

# In[79]:


df.drop("Survived", axis = 1, inplace = True) ##Drop function use delete any column in dataset with axis = 1


# In[80]:


df


# # Delete Rows 

# In[81]:


df.head()


# In[82]:


df.drop(2)


# In[83]:


df.drop(2, inplace = True)


# In[84]:


df.head()


# # Set index function

# In[91]:


df.set_index('Name').head()


# In[90]:


df.set_index('Name', inplace = True).head()


# In[93]:


df.head()


# # Reset index function

# In[95]:


df.reset_index().head()


# # Create a dataframe from the dictionary. 

# In[96]:


a = {"Key1" :[1,2,3,4,5],
     "Key2" :[6,7,8,9,10],
     "Key3" :[11,12,13,14,15]
}


# In[97]:


a


# In[99]:


pd.DataFrame(a)


# # Remove Mising value

# In[101]:


df.dropna().head()


# In[103]:


df.head()


# In[105]:


df.dropna(inplace = True) ##Inplace Function use to delete data permanently 


# In[106]:


df.head()


# In[107]:


df1 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[109]:


df1.head()


# # Replace Function

# In[111]:


df1.fillna('Pal').head()

