from openpyxl import Workbook
import openpyxl as pyxl
def grade_point_from_letter(l):
    l_s_map={"S":9,"S+":10,"O":10,"A":8,"B":7,"C":6,"D":5,"E":4,"F":0}
    
class Student:
    def __init__(self,usn,name):
        self.name=name
        self.usn=usn
        self.subject=[]
    def show_spga_info(self):
        g_c=0
        s_c=0
        for s in self.subjects:
            g_c+=s["C"]*l_s_map[s["G"]]
            s_c+=s["C"]
        si=g_c/s_c
        print(f"Name:{self.name}{si}")

                
wb=pyxl.load_workbook("Result.xlsx")
sheet=wb.active
students=[]
for row in sheet.iter_rows(min_rows=3,min_col=2,max_col=13):
   if row:
       data=[c.value for c in row]
       stu=data[:2]
       sub_1=data[5:7]
       sub_2=data[-2:]
       student=Student(*stu)
       c_1=sub_1[0]
       g_1
       subject=[sub_1,sub_2]
       student.subjet.append({"C":sub_1[0],"G":sub_1[1]})
       student.subjet.append({"C":sub_2[0],"G":sub_2[1]})

for s in students:
    s.show_spga_info() 