import pytest
from SolutionProblem2 import travel_sequence

def test_travel_sequence():
    travel_dict = {"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}
    assert travel_sequence(travel_dict) == ['Bombay->Delhi', 'Delhi->Goa', 'Goa->Chennai', 'Chennai->Banglore']
   
def test_travel_sequence2():
    travel_dict2 = {"Chennai":"Banglore","Banglore":"Goa"}
    assert travel_sequence(travel_dict2) == ['Chennai->Banglore','Banglore->Goa']
