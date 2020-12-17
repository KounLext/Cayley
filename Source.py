#!/usr/bin/env python
# coding: utf-8

# In[4]:


import networkx as nx
import itertools 
import matplotlib.pyplot as plt


# # Группа целых чисел

# In[70]:




class MyError(ValueError):
    def __init__(self, text):
        self.txt = text

class CayZ(nx.Graph):#граф Кэли на целых числах с операцией сложения
    def __init__(self,n,S): 
        if n<=0:
            raise MyError("неподходящее n")
        for s in S:           
            if type(s)!=int:
                raise MyError('используйте целые числа')
            if s>n:
                raise MyError('в порождающем множестве неподходящие элементы')
            if not (-s in S or n-s in S):
                S.append(-s) 

        nx.Graph.__init__(self)
        self.n=n
        self.S=S
        
        nodes=range(n)
        self.add_nodes_from(nodes)
        for v in self.nodes:
            for s in S:
                c=(v+s)%n
                self.add_edge(c,v)
    

n=6
S=[1,4,5]
h=CayZ(n,S)

nx.draw_kamada_kawai(h,
         node_color='y',
         node_size=1000,
         with_labels=True)
print("S:",end="{")
for a in S:
    print(a,end=",")
print("}")
isr=nx.is_distance_regular(h)
if isr:
    print("Граф дистанционно регулярный")


# ### Матрица смежности

# In[71]:


print(nx.adjacency_matrix(h).todense()) #матрица смежности


# ### Спектр

# In[75]:


print("Числа приблизительные")

sp=nx.adjacency_spectrum(h)
for c in sp:
    if c.imag==0:
        print( '%.9f' % c.real, end=",")
    else:
        print(c)    


# ## Симметрическая группа

# In[68]:


def concat(per1,per2):
    res=[]
    for e in per2:
        res.append(per1[e-1])
    return tuple(res)


class CaySym(nx.DiGraph):
    def __init__(self,n,S):
        nx.DiGraph.__init__(self)
        if type(n)!=int:
                raise MyError('используйте целые числа')
        self.n=n
        for s in S:
            if len(s)!=n:
                raise MyError("в порождающем множестве перестановки не той длины")
        self.S=S
        perm=itertools.permutations(range(1,n+1),n)
        self.add_nodes_from(perm)
        nodes=list(self.nodes)
        for node in nodes:
            for s in S:
                self.add_edge(node,concat(node,s))

n=4
S=[(2,3,1,4),(4,1,2,3)]
g=CaySym(n,S)

nx.draw_kamada_kawai(g,
         node_color='y',
         node_size=1000,
         with_labels=True)
isr=nx.is_distance_regular(g)
if isr:
    print("Граф дистанционно регулярный")


# ### Матрица смежности

# In[76]:


print(nx.adjacency_matrix(g).todense()) #матрица смежностb


# ### Спектр

# In[ ]:


print("Числа приблизительные")

sp=nx.adjacency_spectrum(g)
for c in sp:
    if c.imag==0:
        print( '%.9f' % c.real, end=",")
    else:
        print(c)


# ## Недоработанная часть с интерактивом

# In[26]:


from IPython.display import display
import ipywidgets 
rButtons1 = RadioButtons(
    options=['Группа целых чисел', 'Симметрическая группа'],
   # value='Группа целых чисел', # Выбор по умолчанию
    description='Группа:'
)


def on_button_clicked(b):
    if b.value=='Группа целых чисел':
        print(2)

rButtons1.observe(on_button_clicked, names='value')
display(rButtons1)


# In[ ]:




