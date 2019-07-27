class Stack:


    def __init__(self):
        self.st=[]

    def push(self,ele):
        self.st.append(ele)
       
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele=self.st.pop()
            print(f"Element {ele} is removed from stack")    

    def search(self,searchEle):
        if self.is_empty():
            print("Stack empty")
        else:
            for index,ele in enumerate(self.st):
                if ele==searchEle:
                    return index
     
    def show(self):
        if self.is_empty():
            print("Stack empty")
        else:
            print("Elements of stack are:")
            print(self.st)
            

      
    def is_empty(self):
        return len(self.st)==0

if __name__=="__main__":
    st=Stack()
    while True:
        print("1:push, 2.pop, 3.search 4.display 5.exit")
        try:
            ch=int(input("Enter your choice"))
            if ch==1:
                ele=int(input("Enter the element to push"))
                st.push(ele)
            elif ch==2:
                st.pop()
            elif ch==3:
                ele=input("Eneter the element to search")
                res=st.search(ele)
                if res!=1:
                    print(f"element {ele} found at location {res}")
                else:
                    print("element not found")            
            elif ch==4:
                st.show()
            else:
                break    
        except (ValueError,keyError):
            print("Enter only numbers 1-5")    