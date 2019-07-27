products={}
while True:
    print("1.Add 2.viewall 3.search by id 4.exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        pid=int(input("Enter the product id:"))
        pname=input("Enter the product name")
        products[pid]=pname
    elif ch==2:
        if len(products)==0:
            pass
        else:
            for k,v in products:
                print(f"{k}:{v}")
    elif ch==3:
        pid=int(input("Enter the product id:"))
        if products.get(pid):
            print(f"product id:{pid},product name{name}")
        else:
            print("data not found")
    else:
        break            

