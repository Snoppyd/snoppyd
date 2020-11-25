import collections   # 调用collections
a=open("Walden.txt","r").read() # 以只读方式打开并读取瓦尔登湖文件
a=a.split()  # 把a字符串按空格拆分成集合
r=collections.Counter(a) # 按照每个元素出现的次数按照从高到低的顺序排序
print(r) # 输出