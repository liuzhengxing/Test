# encoding: utf-8
class person():
    def work(self):
        return "report"

    def pay(self, report):
        return report+" money"


lzx = person()
workResult = lzx.work()
print(workResult)
payroll = lzx.pay(workResult)
print(payroll)




