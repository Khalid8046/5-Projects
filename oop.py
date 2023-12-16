#OOP IN PYTHON

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100    
        
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
        return value / len(self.students)
    
s1 = Student("Raj", 19, 95)
s2 = Student("Tim", 29, 86)
s3 = Student("Bob", 24, 78)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())





class Pet:
    def __init__(self, name, age):
        self.name= name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am a {self.age} years old")




class Cat(Pet):  
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
        
p = Pet("Bob", 19)
p.show()
c = Cat("Tim", 34)
c.show()
c.speak()





class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
print(Math.add5(10))



class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")
             
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people()
        
Math.pr()
    
print(Math.add5(10))
print(Math.add10(3))