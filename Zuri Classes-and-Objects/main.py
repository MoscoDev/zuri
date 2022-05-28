# from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, score, tracks):
       pass
       self.name = str(name)
       self.age = int(age)
       self.tracks= list(tracks)
       self.score = float(score)
        

    def change_name(self, name):
        print(self.name)

    def change_age(self, age):
    
        print(self.age)

    def add_track(self, track):
        self.tracks.append(track)
        print(self.tracks)

    def get_score(self):
        print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
