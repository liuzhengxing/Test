# encoding: utf-8

class A():
    def funA1(self):
        print("funA1")

    def funA2(self):
        print("funA2")

class B():
    # global a
    a = A()
    def funB1(self):
        B.a.funA1()

    def funB2(self):
        B.a.funA2()

b = B()
b.funB1()
b.funB2()