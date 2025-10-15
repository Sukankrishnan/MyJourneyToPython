numberOne=5_0
numberTwo=1_0_8

def add(numberOne, numberTwo):
    return numberOne+numberTwo

def test_add():
    result = add(numberOne, numberTwo)
    assert result == 10
