# encoding: utf-8
class VarTest():

    num = 1

    def vartest(self):
        print("num")

vartest = VarTest()
def globalvartest():
    print(vartest.num)

globalvartest()
