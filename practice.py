class student ():
    name= ""
    age=13
    grade= "8B"
    house="Slytherin"

    def __init__(self):
        print("new student has been created")

    def update(self):
        print("please enter your name: ")
        self.name=input()
        print("Please enter your age: ")
        self.age=int(input())

    def display(self):
        print("these are the details of the students")
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.house)

student1=student()
student1.update()
student1.display()
