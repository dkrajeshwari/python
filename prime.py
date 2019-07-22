num=int(input("Enter the number"))
is_prime=True
if num<2:
   is_prime=False
else:
   for i in range(2,num//2+1):
      if num % i==0:
         is_prime=False
         break

if is_prime:
   print(f"{num} is prime number")
else:
   print(f"{num} is not  a prime number")               