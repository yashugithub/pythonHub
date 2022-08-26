import functools

def iden(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('------------before-------')
        res = func(*args, **kwargs)

        print('----------------------after-----------------')
        return res
    return wrapper

def add(x, y):
    print('---------------in add function--------------')
    return x+y

def heelo_world():
    print('hello world')
