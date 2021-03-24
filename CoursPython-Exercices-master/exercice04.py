def get_category(age):
    if age>=6 and age<=7:
        return "Poussin"
    elif age>=8 and age<=9:
        return "Pupille"
    elif age>=10 and age<=11:
        return "Minime"
    elif age>=12:
        return "Cadet"
    else :
        raise ValueError


def run():
    assert get_category(6) == "Poussin"
    assert get_category(7) == "Poussin"
    assert get_category(8) == "Pupille"
    assert get_category(9) == "Pupille"
    assert get_category(10) == "Minime"
    assert get_category(11) == "Minime"
    assert get_category(12) == "Cadet"
    assert get_category(99) == "Cadet"
    
    try:
        get_category(1)
        raise AssertionError()
    except ValueError:
        pass
