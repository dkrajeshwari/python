#program to calculate the electric bill
 
#min bill 50rupee
#1-500 6rupees/unit
#501-1000 8rupees/unit
#>1000 12rupees/unit

units=int(input("Enter the number of units:"))
if units>=1 and units<=500:
   rate=6
elif units>=501 and units<=1000:
   rate=8
elif units>1000:
   rate=12
amount=units*rate
if amount<50:
   amount=50
print(f"Units used:{units},Bill amount:{amount}")
