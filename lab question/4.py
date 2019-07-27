def is_prime(N):
   if N<2:
      return False
   for i in range (2,N//2+1):
        if N%i==0:
            return False
   return True

LB=int(input("Enter  lower bound:"))
UB=int(input("Enter upper bound:"))
for i in range(LB,UB+1):
   if is_prime(i):
      print(i)




