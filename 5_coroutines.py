def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)

def aaa():
    yield from 'oleg'


a = aaa()
print(next(a))
print(next(a))
print(next(a))
