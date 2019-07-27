
count=0
num=int(input("Enter the umber"))
while num!=0:
    r=num%10
    if r in [2,3,5,7]:
        count+=1
    num=num//10
print(count)    