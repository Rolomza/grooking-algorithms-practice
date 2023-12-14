from binary_search import *

def test_item_in_list():
    assert binary_search([1,2,3],2) == 1

def test_item_not_in_list():
    assert binary_search([1,2,3],5) == None