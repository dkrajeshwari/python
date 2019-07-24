from emp import Employee
lst_emp=[]
def load_emp():
    with open("emp.txt") as f:
        fdata=f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno=int(edata[0])
            ename=edata[1]
            qual=edata[2]
            sal=int(edata[3])
            dept_name=edata[4]
            emp=Employee(empno,ename,qual,sal,dept_name)
            lst_emp.append(emp)
    print(f"Total Employee Count:{len(lst_emp)}")


def showDeptNames():
    dnames=set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)            

def showAllQualifications():
    qualifications=set(map(lambda emp:emp.qual,lst_emp))
    for qual in qualifications:
        print(qual)

def maxSalaryEmp():
    max_sal=max(list(map(lambda x:x.sal,lst_emp)))
    lst=list(filter(lambda x:x.sal==max_sal,lst_emp))
    for emp in lst:
        emp.show_info()
        
def showEmpCountByDeptName():
    pass
def showTotalSalByDeptName():
    pass            
def showEmpCountByQual():
    pass


load_emp()
print("All dept names:")         
showDeptNames()   
print("All qualifications") 
showAllQualifications() 

