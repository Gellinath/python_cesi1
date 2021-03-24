def is_number_correct(number):
    a=0
    if number >=10 and number<=20 :
        return True, a
    elif number>20 :
        a = number -20
        a= -a
        return False, a
    elif number<10 :
        myNumber = number
        while myNumber<10 :
            a +=1
            myNumber +=1
        return False, a
    return

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)
