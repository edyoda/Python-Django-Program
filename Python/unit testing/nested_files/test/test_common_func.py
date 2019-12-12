from src.code.common_func import *
import pytest

@pytest.mark.regression
def test_key_present_ls():
    l = [10,20,30,40,50,60]
    key = 30 
    result = linear_search(l,key)
    assert False == result
    
@pytest.mark.parametrize("l,key,expected_ans",[([10,20,30,40,50,60],400,False),([100,200,300,400,500,600],4000,False),([100,200,300,400,500,600],4000,False)])
def test_key_not_present_ls(l,key,expected_ans):

    result = linear_search(l,key)
    assert expected_ans == result