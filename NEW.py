class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # A list to store multiple numeric grades

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print(f"Invalid score: {score}. Please enter a value between 0 and 100.")

    def calculate_average(self):
        if not self.grades:
            return 0
        # This uses the same math logic as finding a resultant or mean
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        # Using the "Identity Card" trick we discussed
        avg = self.calculate_average()
        return f"Student: {self.name} | Average: {avg:.2f}"


class Classroom:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # Our list of Student objects

    def enroll_student(self, student_obj):
        self.students.append(student_obj)
        print(f"Enrolled {student_obj.name} in {self.course_name}.")

    def get_top_student(self):
        if not self.students:
            return "No students enrolled."

        # We assume the first student is the top one, then compare
        top_student = self.students[0]

        for student in self.students:
            if student.calculate_average() > top_student.calculate_average():
                top_student = student

        return f"The top student is {top_student.name} with an average of {top_student.calculate_average():.2f}"

# 1. Create the Classroom
my_class = Classroom("Object-Oriented Programming")

# 2. Create Student Objects
john = Student("John Luis") # cite: 1
maria = Student("Maria")

# 3. Add some grades
john.add_grade(85)
john.add_grade(92)
maria.add_grade(95)
maria.add_grade(88)

# 4. Enroll them
my_class.enroll_student(john)
my_class.enroll_student(maria)

# 5. Find the winner
print(my_class.get_top_student())