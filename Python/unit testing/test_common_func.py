from common_func import linear_search
import pytest

@pytest.mark.regression
def test_key_present_ls():
    l = [10,20,30,40,50,60]
    key = 30 
    result = linear_search(l,key)
    assert False == result
    
def test_key_not_present_ls():
    l = [10,20,30,40,50,60]
    key = 300 
    result = linear_search(l,key)
    assert False == result