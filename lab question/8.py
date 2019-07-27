num=int(input("enter the number"))
while num!=0:
    digit=num%10
    if digit in [2,3,5,7]:
        print(digit,end=" ")
    num//=10    