import pytest
from Problem2 import travel_sequence

def test_travel_sequence():
    travel_dict = {"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}
    assert travel_sequence(travel_dict) == ['Bombay->Delhi', 'Delhi->Goa', 'Goa->Chennai', 'Chennai->Banglore']


