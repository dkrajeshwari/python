data="raji,sony,anu,arpitha"
x=list(map(lambda x:x.capitalize(),data.split(",")))
print(list(filter(lambda x:x.startswith("A"),x)))
