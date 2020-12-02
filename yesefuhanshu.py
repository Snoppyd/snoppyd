#!/usr/bin/env python
# coding: utf-8

# In[4]:


def play(players,step,alive):


    """
    Input：
    players：参加游戏的人数；
    step：数到step数字的人淘汰；
    alive：幸存人数，即游戏结束。

    Output：
    返回一个列表，列表中元素为幸存者的编号

    """
    A = [i for i in range(1,players+1)]
    B = 0
    while len(A)>alive:
        i = 0
        while i <len(A):
            B += 1
            if B == step:
                A.remove(A[i])
                B = 0
            else:
                i += 1
            
    return A
players = int(input("参加游戏的人数："))
step = int(input("数到多少的人淘汰："))
alive = int(input("游戏结束，幸存人数为："))
play(players,step,alive)


# In[ ]:





# In[ ]:




