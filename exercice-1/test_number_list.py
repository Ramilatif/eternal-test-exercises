from number_list import convert_to_integer
import pytest

def verif_int(list):
    return all(isinstance(element,int) for element in list)

def test_convert_to_integer (): 

    test_list = ['5',"1",7,"ye",'1.02']
    assert(verif_int(convert_to_integer(test_list)) ) == True