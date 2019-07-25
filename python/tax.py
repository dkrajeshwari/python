#program to calculate income tax
income=float(input("Enter the income"))
if income<500000:
   tax_rate=0
elif income>500000 and income<1000000:
   temp=income-500000
   tax_amount=temp*0.1
elif income>1000000:
   temp=income-500000
   if temp>500000 and temp<1000000:
      tax_amount=temp*0.1
      temp=temp-1000000
   if temp>0:
      tax_amount+=temp*0.3

print(f"Income:{income},tax amount:{tax_amount}")

