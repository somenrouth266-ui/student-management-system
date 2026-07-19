#project #8
#student management system using mysql and python
import mysql.connector
db=mysql.connector.connect(
    host="localhost",user="root",
    password="ritvick123",
    database="asteroid"
)
print("connected")
cursor= db.cursor()
while True:
    print("\n Student management system")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice=int(input("Enter choice:"))
    if choice == 1:
        name=input("Name:")
        age=int(input("Age:"))
        course=input("Course:")
        sql="Insert into student (name,age,course) values(%s,%s,%s)"
        cursor.execute(sql,(name,age,course))
        db.commit()
        print("Student added successfully!")
    elif choice == 2:
        cursor.execute("Select * from student")
        student=cursor.fetchall()
        print("\nid\tname\tage\tcourse")
        for s in student:
         print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}")
    elif choice == 3 :
                name=input("Enter student name:")
                cursor.execute("Select * from student where name = %s",(name,))
                studentt=cursor.fetchone()
                if studentt:
                    print(studentt)
                else:
                    print("Student not found")
    elif choice == 4:
                sid=int(input("Student id:"))
                new_course=input("New course:")
                cursor.execute("Update student set course=%s where id = %s",(new_course,sid))
                db.commit()
                print("Updated successfully")
    elif choice == 5:
        sid=int(input("Student id:"))
        cursor.execute("delete from student where id=%s",(sid,))
        db.commit()
        print("Deleted successfully")
    elif choice == 6:

        print("Goodbye")
        break
    else:
        print("Invalid")
db.close()