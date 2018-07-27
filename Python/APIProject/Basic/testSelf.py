#encoding = utf-8

class AAA():
    def go(self):
        self.one = 'hello'

class BBB():
    def go(self):
        one = 'hello'

a1 = AAA()
a1.go()
print(a1.one)

b1 = BBB()
print(b1.go())

def run(self):
    print(self)

run(1)