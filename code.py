
# coding: utf-8

# In[71]:


import pandas as pd
p=pd.read_csv("housing.csv")


# In[72]:


from sklearn.cross_validation import train_test_split


# In[73]:


X_train,X_test=train_test_split(p,test_size=0.75)


# In[74]:


print len(X_train),len(X_test)


# In[80]:


def plot_(*args):
    import matplotlib.pyplot as plt
    v1,v2=args
    plt.scatter(X_train[v1],X_train[v2])
    plt.show()
columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
# for i in columns:
#     plot_(i,'MEDV')

