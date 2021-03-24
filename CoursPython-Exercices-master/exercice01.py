a = 1
b = 2

a, b = b, a

def run():
    assert a == 2
    assert b == 1
