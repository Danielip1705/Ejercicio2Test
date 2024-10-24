from Ejercicio2 import formulaVel

def test_FormulaVel_1():
    assert formulaVel("D=5","T=5")=="V=1"

def test_FormulaVel_2():
    assert formulaVel("V=10","T=2")=="D=20"

def test_FormulaVel_3():
    assert formulaVel("V=5","D=10")=="T=2"

def test_FormulaVel_4():
    assert formulaVel("D=32","T=4")=="V=8"

def test_FormulaVel_5():
    assert formulaVel("T=4","V=8")=="D=32"

def test_FormulaVel_6():
    assert formulaVel("V=8","D=32")=="T=4"
    
def test_FormulaVel_7():
    assert formulaVel("v=8","d=32")=="T=4"





