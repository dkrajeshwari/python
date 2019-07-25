lst=[]
def add(ele):
    lst.append(ele)
def delete():
    if len(lst)==0:
        print("list empty")
    else:
        ele=lst.pop()
        print(f"element deleted is {ele}")
def search(ele):
    if len(lst)==0:
        print("list empty")
    else:
        if ele in lst:
            index=lst.index(ele)
            print(f"elem {ele} found at {index}")
        else:
            print(f"given {ele} not found")
def display():
       if len(lst)==0:
          print("list empty")
       else:
            #for i in lst:
                print(lst)
while True:
    print("****1:add 2:delete 3:search 4:display 5:exit*****")
    ch=int(input("Enter your choice"))
    if ch == 1:
        ele=int(input("Enter the ele"))
        add(ele)
    elif ch ==2:
        ele=delete()
     
    elif ch ==3:
        ele=int(input("enter the ele to search"))
        search(ele)
    elif ch == 4:
        display()
    else:
        print("thank you")
        break    



