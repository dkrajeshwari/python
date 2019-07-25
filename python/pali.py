#program to check weather given number is palindrome or not

N=int(input("Enter the number"))
rev=0
temp=N
while temp>0:
   rev=rev*10+(temp%10)
   temp=temp//10
if rev==N:
   print(f"{N} is palindrome")
else:
   print(f"{N} is not palindrome")