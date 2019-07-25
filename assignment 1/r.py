import randint as rn
ls=[]
for i in range(1,101):

    ls.append(rn.randint(1,1000))
for i in ls:
    if i%3==0 and i% 6==0 and i%9!=0:
        print(i)
