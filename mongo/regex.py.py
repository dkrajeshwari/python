import re

data="1001 DBMS 20 1002 JS 23 1003 SQL 15"
lst=re.findall(r"\s+",data)
print(lst)
lst1=re.findall(r"[A-Z]+",data)
print(lst1)
lst2=re.findall(r"\d{4}",data)
print(lst2)


data1="raji is in 56007 works at Bangalore and sony is 3456 at Mangalore"
lst3=re.findall(r"\d{5}",data1)
print(lst3)
lst4=re.findall(r"at\s+([A-z]*)\s?",data1)
print(lst4)    



