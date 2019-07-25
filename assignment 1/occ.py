names=["raji","sony","arpi","madhu","raj","yash"]
c_names={}
for name in names:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]+=1
print(c_names)            
