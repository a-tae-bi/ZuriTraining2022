from re import A


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks =  { }
        self.score = float(score)
        print("The student\'s details are:\n""Student name:",name, "\nStudent age:",age, "\nStudent track:",tracks, "\nStudent score:",score)
        
    def change_name(self, new_name):
        self.name = new_name
        print("The student\'s new name:\n",new_name)

    def change_age(self, new_age):
        self.age = new_age
        print("The student\'s new age:\n",new_age)

    def add_track(self, new_track):
        self.track = new_track
        print("The student\'s track is:\n",new_track)
    
    def get_score(first_student):
        print("The student\'s score is:\n",first_student.score)     

# first_student = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
first_student =  Student("Bob", 26.90, ["FE","BE"],20.90)
first_student

# Expected methods
first_student.change_name("Peter")
first_student.change_age(34)
first_student.add_track("UI/UX")
first_student.get_score()
