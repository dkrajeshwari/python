num=int(input("Enter the number"))
rev=0
temp=num
while num!=0:
    rev=rev*10+num%10
    num//=10

print(f "reverse of {temp} the number is {rev}")    