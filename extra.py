class people:
    def __init__(self, grade, name,behavior):
        self.grade = grade
        self.name = name
        self.behavior = behavior
    def actions(self, subject):
        print(f"{self.name} is studying {subject} and get {self.grade} at the course.")
class student(people):
    def __init__(self, grade, name, behavior):
        super().__init__(grade, name, behavior)

    def study(self, subject):
        return f"{self.name} is studying {subject} and get {self.grade} at the course."
    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.action} right now."
Ammy = student("A","Alice","reading")
print(Ammy.study("Math"))
Bob = student("B","Bob","running")
print(Bob.actions("Science"))
    


        
