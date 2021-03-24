def factorial(number):
    a=1
    b=1
    if number>=0 :
        
        for i in range(number) :
            b= b*a
            a+=1
    elif number<0 :
        a=-1
        b=-1
        for i in range(-number) :
            b= b*-a
            a-=1
    return b

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320
