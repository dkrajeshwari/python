data="parth,anith,sapna,raji,Anitha,vinith"
print(data)
lst=[]
names=data.upper().split(",")
for name in names:
    if name.startswith("A") or name.endswith("H"):  
         lst.append(name)
lst.sort(reverse)
print(lst)

