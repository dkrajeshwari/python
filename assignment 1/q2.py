#program to find the sum of series of factorial

N=int(input("Enter the number:"))
sum=0
for i in range (1,N+1):
  
   for j in range(1,i+1):
      
   sum+=1/i
print(f"result is {sum}")

