import sqlite3
host_name="data.db"
def create_table():
    try:
        conn=sqlite3.connect(host_name)
        cursor=conn.cursor()
        cursor.execute("Create table student(regno integer primary key,name text,sem integer,placed integer)")
        conn.close()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()
def add_new_student(regno,name,sem,placed):
    try:
        conn=sqlite3.connect(host_name)
        cursor=conn.cursor()
        cursor.execute("insert into student(regno,name,sem,placed) values(?,?,?,?)",(regno,name,sem,placed))
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close() 
def show_students():
    try:
        conn=sqlite3.connect(host_name)
        cursor=conn.cursor()
        cursor.execute("select regno,name,sem,placed from student")
        rows=cursor.fetchall()
        for row in rows:
            status="placed" if row[2]==1 else "not placed"
            print(f"{row[0]},{row[1]},{row[3]},and {status}")
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close() 
def update_stu_status(regno,placed):
    try:
        conn=sqlite3.connect(host_name)
        cursor=conn.cursor()
        cursor.execute("update student set placed=? where regno=?",(placed,regno))
        conn.commit()
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()   

def query_1(regno):
    try:
        conn=sqlite3.connect(host_name)
        cursor=conn.cursor()
        cursor.execute("select regno,name,sem,placed from student where regno=?",(regno,))
        row=cursor.fetchone()
        if row:
            status="placed" if row[3]==1 else "not placed"
            print(f"{row[0]},{row[1]},{row[2]},and {status}")
        else:
            print(f"not found")    
    except Exception as e:
        print(f"{str(e)}")
    finally:
        conn.close()              

#create_table()
#add_new_students(2,'sony',7,0)
#show_students()
#update_stu_status(1,1)
#show_students()
query_1(1)