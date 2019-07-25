amount=float(input("Enter the amount:"))
if amount>=10000:
   discount = amount*0.2
else:
   discount=amount*0.05
net_amount=amount-discount
print(f"Bill amount:{amount},discount:{discount},Net Amount:{net_amount}")