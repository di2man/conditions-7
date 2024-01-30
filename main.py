class Person:
    def __init__(self, name, age, gender, address, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.email = email

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}, Email: {self.email}"


class Teacher(Person):
    def __init__(self, name, age, gender, address, email, subjects_taught, experience, office):
        super().__init__(name, age, gender, address, email)
        self.subjects_taught = subjects_taught
        self.experience = experience
        self.office = office

    def conduct_lesson(self, subject, duration):
        print(f"Teacher {self.name} is conducting a {subject} lesson for {duration} minutes.")

    def assess_students(self, student, grades):
        print(f"Teacher {self.name} is assessing {student.name}. Grades: {grades}")


class Student(Person):
    def __init__(self, name, age, gender, address, email, course, group, average_grade):
        super().__init__(name, age, gender, address, email)
        self.course = course
        self.group = group
        self.average_grade = average_grade

    def attend_lectures(self, subject):
        print(f"Student {self.name} is attending {subject} lectures.")

    def get_grades(self):
        # Логіка отримання оцінок (припустимо, що студент вже має оцінки)
        return {"Math": 90, "History": 85, "English": 92}


class Subject:
    def __init__(self, name, code, subject_type):
        self.name = name
        self.code = code
        self.subject_type = subject_type

    def get_info(self):
        return f"Subject: {self.name}, Code: {self.code}, Type: {self.subject_type}"


class Academy:
    def __init__(self, name, foundation_year, address):
        self.name = name
        self.foundation_year = foundation_year
        self.address = address
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        self.teachers.remove(teacher)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def organize_exam(self, subject):
        print(f"The academy is organizing an exam for {subject}.")


math_teacher = Teacher("John Smith", 35, "Male", "123 Main St", "john@example.com", ["Math"], 10, "Room 101")
history_teacher = Teacher("Alice Johnson", 40, "Female", "456 Oak St", "alice@example.com", ["History"], 15, "Room 202")

student1 = Student("Bob Johnson", 20, "Male", "789 Pine St", "bob@example.com", 2, "A", 88)
student2 = Student("Emily Davis", 22, "Female", "101 Elm St", "emily@example.com", 3, "B", 92)

math_subject = Subject("Mathematics", "MATH101", "Compulsory")
history_subject = Subject("History", "HIST201", "Elective")

academy = Academy("My Academy", 2000, "789 Oak St")


academy.add_teacher(math_teacher)
academy.add_teacher(history_teacher)
academy.add_student(student1)
academy.add_student(student2)


academy.organize_exam(math_subject)


math_teacher.conduct_lesson("Mathematics", 60)
math_teacher.assess_students(student1, {"Math": 85, "Homework": 90})


student1.attend_lectures("Mathematics")
grades = student1.get_grades()
print(f"{student1.name}'s grades: {grades}")
