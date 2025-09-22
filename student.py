# TODO create class Student

class Student:
    def __init__(self,Name,Grade):
        self.Name=Name
        self.Grade=Grade
    def get_name(self):
        return self.Name
    def get_grade(self):
        return self.Grade
    def set_grade(self,new):
        self.Grade=new
        return self.Grade
