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