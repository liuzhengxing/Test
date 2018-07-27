#encoding = 'utf-8'

class Student():
    def get_grade(self,score):
        if score > 90:
            return "A"

        if 60< score < 90:
            return "B"

        if score < 60:
            return "C"

simba = Student()
result = simba.get_grade(60)
print(result)

class AAA(object):
    def go(self):
        self.one = "hello"

class BBB(object):
    def go(self):
        one = "hello"

A1 = AAA()
A1.go()
A1.one

B1 = BBB()
B1.go()

