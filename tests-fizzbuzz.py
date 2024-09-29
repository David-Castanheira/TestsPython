import pytest 
from controllers.fizzbuzz import fizzbuzz

def test_case1():
    assert fizzbuzz(1)[0] == 1

def test_case2():
    assert fizzbuzz(2)[1] == 2

def test_case3():
    assert fizzbuzz(3)[2] == 'Fizz'

def test_case4():
    assert fizzbuzz(4)[3] == 4

def test_case5():
    assert fizzbuzz(5)[4] == 'Buzz'

def test_case6():
    assert fizzbuzz(6)[5] == 'Fizz'

def test_case7():
    assert fizzbuzz(7)[6] == 7

def test_case8():
    assert fizzbuzz(8)[7] == 8

def test_case9():
    assert fizzbuzz(9)[8] == 'Fizz'

def test_case10():
    assert fizzbuzz(10)[9] == 'Buzz'

def test_case11():
    assert fizzbuzz(11)[10] == 11

def test_case12():
    assert fizzbuzz(12)[11] == 'Fizz'

def test_case13():
    assert fizzbuzz(13)[12] == 13

def test_case14():
    assert fizzbuzz(14)[13] == 14

def test_case15():
    assert fizzbuzz(15)[14] == 'FizzBuzz'

def test_case16():
    assert fizzbuzz(16)[15] == 16

def test_case17():
    assert fizzbuzz(17)[16] == 17

def test_case18():
    assert fizzbuzz(18)[17] == 'Fizz'

def test_case19():
    assert fizzbuzz(19)[18] == 19

def test_case20():
    assert fizzbuzz(20)[19] == 'Buzz'