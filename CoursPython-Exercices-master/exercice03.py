def is_product_negative(a, b):
    c = a*b
    if c<0 :
        return True
    else :
        return False

def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False
