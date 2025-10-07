numberOne=5
numberTwo=10

def add(numberOne, numberTwo):
    return numberOne+numberTwo

def test_add():
    result = add(numberOne, numberTwo)
    assert result == 10
