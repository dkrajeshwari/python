
def amstrong_num(num):
    num_1=num
    res=0
    while num!=0:
        r=num%10
        res=res+r**3
        num=num//10
    return num_1==res

input_num=int(input("Enter the number"))
if amstrong_num(input_num):
    print(f"Given number {input_num} is an amstrong number")
else:
       print(f"Given number {input_num} is  not amstrong number")            