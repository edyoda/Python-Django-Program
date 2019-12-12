
from src.code.common_func import *
import pytest

def test_add():
    num1 = 10
    num2 = 20
    result = add(num1,num2)
    assert 30 == result
    
@pytest.mark.regression
def test_sub():
    num1 = 100
    num2 = 20
    result = sub(num1,num2)
    assert 80 == result
    