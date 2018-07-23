# encoding: utf-8
kwargs = {}
kwargs.setdefault('method', 'POST')
kwargs.setdefault('url', '/ime-container/imePlanOrder/insertPlanOrder.action')
kwargs.setdefault('data', '123')

print(kwargs.keys())
print(kwargs.pop('method'))
print(kwargs)

class Plan():
    i = 1

class Test():
    def tearDown(self):
        PO = Plan()


