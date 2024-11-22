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
        self.grades = []

    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
    
    def add_grade(self, grade):
        self.grades = self.grades.append(grade)
    
    def calculate_average_grade(self):
        len = len(self.grades)
        sum = sum(self.grades)
        avg_grade = len / sum
        return avg_grade
    
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
                super().__init__(self, given_name, given_age, given_gender)
                self.admin_id = ""
                self.office = ""
                self.years_of_service = ""
            
            def set_admin_details(self, admin_id, office, years_of_service):
                self.admin_id = admin_id
                self.office = office
                self.years_of_service = years_of_service
            
            def 