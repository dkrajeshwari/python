def sum1(num):
    res=0
    while num!=0:
        r=num%10
        res+=r
        num=num//10
    if res<10:
        return res
    else:
        new_num=res
        ans=sum1(new_num)
        return ans

num=int(input("Enter the number"))
sum=sum1(num)
print(f"result={sum}")



OR



#tnum=num=int(input("Enter the number:"))
#while num>9:
    #sum=(num%10+num//10)
    #num=sum
#print(f"the sum of digits of {tnum} is';{num}")    