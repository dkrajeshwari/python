num=tnum=int(input("Enter the number"))
n=4
res=0
while n>=0:

    q=tnum//(10**n)
    tnum=tnum%(10**n)
    if q==9:
        q=0
    else:
        q+=1    
    res+=q*(10**n)
    n=n-1
print(res)        