class Person:
    def __init__(self, given_name, given_age, given_gender):
        self.name = given_name
        self.age = given_age
        self.gender = given_gender
    
    def set_details(self, new_name, new_age, new_gender):
         self.name = new_name
         self.age = new_age
         self.gender = new_gender
    
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student(Person):
    def __init__(self, given_name, given_age, given_gender):
        super().__init__(given_name, given_age, given_gender)
        self.student_id = ""
        self.course = ""
        self.grades = [0]

    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
    
    def add_grade(self, grade):
        self.grades = self.grades.append(grade)
    
    def calculate_average_grade(self):
        for x in int(str(self.grades)):
            summ = sum(x)
            return summ
        count = 0
        for z in self.grades:
            count += 1
            z = count
        avg = x / z
        return avg
    
    def get_student_summary(self):
        print(f"Name: {self.name}, Student ID: {self.student_id}, Course: {self.course}, Grades: {self.grades} ")
    
class Professor(Person):
    def __init__(self,given_name, given_age, given_gender):
        super().__init__(given_name, given_age, given_gender)
        self.staff_id = ""
        self.department = ""
        self.salary = ""
    
    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    
    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")
    
    def increase_salary(self, percentage):
        multiplier = percentage / 100
        new_salary = self.salary * multiplier
        self.salary = new_salary
    
    def get_professor_summary(self):
        print(f"Name: {self.name}, Staff ID: {self.staff_id}, Department: {self.department}, Salary: {self.salary}")
    
class Administrator(Person):
    def __init__(self, given_name, given_age, given_gender):
        super().__init__( given_name, given_age, given_gender)
        self.admin_id = ""
        self.office = ""
        self.years_of_service = 0
    
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    
    def increment_service_years(self):
        self.years_of_service += 1

    def get_admin_summary(self):
        print(f"Name: {self.name}, Admin ID: {self.admin_id}, Office: {self.office}, Years Of Service: {self.years_of_service}")
        
may = Student("May", 19, "Female")
ben = Student("Ben", 21, "Male")
otto = Professor("Otto", 39, "Male")
osborn = Professor("Osborn", 44, "Male")
thompson = Administrator("Thompson", 41, "Male")

may.add_grade(9)
# may.calculate_average_grade()
otto.give_feedback(may, "Well Done on getting an A in your Midterm.")
otto.set_professor_details("ABD333", "Physics", 1500)
otto.increase_salary(4)
thompson.increment_service_years()

may.get_student_summary()
ben.get_student_summary()
otto.get_professor_summary()
osborn.get_professor_summary()
thompson.get_admin_summary()
