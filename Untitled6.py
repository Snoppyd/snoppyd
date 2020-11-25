#!/usr/bin/env python
# coding: utf-8

# # 代码整合

# 猜数字

# In[ ]:


get_ipython().run_cell_magic('writefile', 'guess.py', 'import random\n\nsecret = random.randint(1, 100)\nguess = int(input("猜猜是哪一个数字："))\nif guess == secret:\n    print("不错哦，猜对了")\nelse:\n    i = 1\n    while (guess != secret) and (i < 5):\n        if guess > secret:\n            guess = int(input("昂，大了，请重新输入："))\n        else:\n            guess = int(input("嘿，小了，请重新输入："))\n        i += 1\n    if guess == secret:\n        print("不错哦，猜对了")\n    else:\n        print("猜数失败，游戏结束。")')


# 随机找同学

# In[2]:


di = {}
import random
m = random.randint(1,39)
print(stu)


# In[ ]:


get_ipython().run_cell_magic('writefile', 'suiji.py', '# 创建一个字典stu，key是学号，value是姓名\n# 学生信息在stu.csv文件里，从文件中读取并保存到字典\n# 打开stu.csv文件\nfile = open(\'C:/Users/Administrator/Desktop/stu.csv\',\'r\')\n\n# 读取文件内容\nlines = file.readlines()\n\n# 抽取每行的学号和姓名，保存到字典\nstu = {}\nfor line in lines:\n    tmp_list = line.split(\',\')\n    xuehao = tmp_list[0]\n    xingming = tmp_list[1]\n    stu[xuehao] = xingming\n\n\n# 从学号中随机抽取n个学号\nimport random\nnum = int(input("输入随机抽取人数："))\n\n# 如何把字典中的key（学号）取成列表\nxuehao_list = random.sample(stu.keys(),num)\nxuehao_list\n\n# 根据随机抽取得到学号，打印输出对应的姓名\nfor xuehao in xuehao_list:\n    print(stu[xuehao])')


# 英文文档词频统计排序

# In[ ]:


get_ipython().run_cell_magic('writefile', 'cipin.py', 'import collections   # 调用collections\na=open("Walden.txt","r").read() # 以只读方式打开并读取瓦尔登湖文件\na=a.split()  # 把a字符串按空格拆分成集合\nr=collections.Counter(a) # 按照每个元素出现的次数按照从高到低的顺序排序\nprint(r) # 输出')


# 行号添加

# In[ ]:


line = 0
nimber = 1
a = open("demo.py","r").readlines()
b = open("demo_new.py","w")
for i in a:
    if(line<len(i)):
        line = len(i)
for i in a:
    i = i.ljust(line+1).replace('\n','')+"#"+str(nimber)+"\n"
    nimber=nimber+1
    b.write(i)

