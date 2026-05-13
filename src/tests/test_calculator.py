"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

my_calculator = Calculator()
def test_app():
    
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    assert my_calculator.addition(2, 3) == 5

def test_fail_addition():
    assert my_calculator.addition(2, 3) != 6
    
def test_subtraction():
    assert my_calculator.subtraction(5, 2) == 3
    
def test_negative_subtraction():
    assert my_calculator.subtraction(2, 5) == -3
    
def test_fail_negative_subtraction():
    assert my_calculator.subtraction(2, 5) != 3
    
def test_fail_subtraction():
    assert my_calculator.subtraction(5, 2) != 4

def test_multiplication():
    assert my_calculator.multiplication(4, 3) == 12

def test_fail_multiplication():
    assert my_calculator.multiplication(4, 3) != 11

def test_multiplication_by_zero():
    assert my_calculator.multiplication(4, 0) == 0

def test_division():
    assert my_calculator.division(10, 2) == 5

def test_fail_division():
    assert my_calculator.division(10, 2) != 6

def test_division_by_zero():
    assert my_calculator.division(10, 0) == "Erreur : division par zéro"
    
def test_addition_subtraction_multiplication_division():
    nb1 = 674480216
    nb2 = 910891864
    nb3 = 796574454
    nb4= 5879
    nb5 = 772890207209
    total = my_calculator.addition(nb1, nb2)
    assert total == 1585372080    
    total = my_calculator.subtraction(total, nb3)
    assert total == 788797626
    total = my_calculator.multiplication(total, nb4)
    assert total == 4637341243254
    total = my_calculator.division(total, nb5)
    assert total == 6
    