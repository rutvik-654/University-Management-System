class person:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(rollno, name)
        self.branch = branch

class teacher(person):
    def __init__(self, rollno, name, subject):
        super().__init__(rollno, name)
        self.subject = subject

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def search_student(self, rollno):
        for s in self.students:
            if s.rollno == rollno:
                return s
        return None
    
    def search_teacher(self, rollno):
        for t in self.teachers:
            if t.rollno == rollno:
                return t
        return None

colleges = []
while True:
    print("Choose the Required option: ")
    print("1. Create College.")
    print("2. Add Student.")
    print("3. Add Teacher.")
    print("4. Display Students.")
    print("5. Display Teachers.")
    print("6. Search Student by Roll No.")
    print("7. Search Teacher by Roll No.")
    print("8. Exit.")
    x = int(input("Enter your Option: "))
    
    if x == 1:
        clgname = input("Enter College Name: ")
        if any(clg.cname == clgname for clg in colleges):
            print("\nCollege Already Exists!\n")
        else:
            colleges.append(college(clgname))
            print("\nCollege Added Successfully\n")
    
    elif x == 2:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll no: ")
            name = input("Enter Student Name: ")
            branch = input("Enter Student Branch: ")
            clg.add_student(student(rollno, name, branch))
            print("\nStudent Added Successfully\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x == 3:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            rollno = input("Enter Roll no: ")
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            clg.add_teacher(teacher(rollno, name, subject))
            print("\nTeacher Added Successfully!\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x == 4:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            if clg.students:
                for i, s in enumerate(clg.students, 1):
                    print(f"Student {i}:\nRoll Number: {s.rollno}\nName: {s.name}\nBranch: {s.branch}\n")
            else:
                print("\nNo Students Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x == 5:
        clgname = input("Enter College Name: ")
        clg = next((c for c in colleges if c.cname == clgname), None)
        if clg:
            if clg.teachers:
                for i, t in enumerate(clg.teachers, 1):
                    print(f"Teacher {i}:\nRoll Number: {t.rollno}\nName: {t.name}\nSubject: {t.subject}\n")
            else:
                print("\nNo Teachers Found!\n")
        else:
            print("\nCollege Does Not Exist!\n")
    
    elif x == 6:
        rollno = input("Enter Student Roll No: ")
        found = False
        for clg in colleges:
            student = clg.search_student(rollno)
            if student:
                print(f"\nStudent Found in {clg.cname}:\nRoll No: {student.rollno}\nName: {student.name}\nBranch: {student.branch}\n")
                found = True
                break
        if not found:
            print("\nStudent Doesn't Exist!\n")
    
    elif x == 7:
        rollno = input("Enter Teacher Roll No: ")
        found = False
        for clg in colleges:
            teacher = clg.search_teacher(rollno)
            if teacher:
                print(f"\nTeacher Found in {clg.cname}:\nRoll No: {teacher.rollno}\nName: {teacher.name}\nSubject: {teacher.subject}\n")
                found = True
                break
        if not found:
            print("\nTeacher Doesn't Exist!\n")
    
    elif x == 8:
        break
    
    else:
        print("\nChoose the Correct Option!\n")
