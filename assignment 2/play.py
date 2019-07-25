c=["1","2","3"]
f=["2","4","3"]
b=["1","5","7"]
lst=[]
lst.extend(c)
lst.extend(f)
lst.extend(b)
print(lst)
new=[]
for n in lst:
    if n not in new:
        new.append(n)
    else:
        pass
print(new)