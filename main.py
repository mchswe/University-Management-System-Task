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
        self.student_id = "00000"
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
        print(f"Name: ")