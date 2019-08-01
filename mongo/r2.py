import re

data="house number 198 and pincode 560070"
res=re.search("\d+",data)
print(data[res.start():res.end()])
print(res.group())


data1="blue shape red toy green"
data1=re.sub('(blue|green|red|yellow)','color',data1)
print(data1)

data2="1001 dbms 20 1002 js 23 1003 sql 15"
lst=re.findall('(\d{4})\s([A-z]*)\s+(\d{2})',data2)
print(lst)  


data3="raji and madhu are good friends ,sony and sona are good friends"
lst1=re.findall(r'bA[a-z]{4}',data3)
print(lst1)