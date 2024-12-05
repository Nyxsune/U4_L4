# # Implementation & testing of the ArrayStack class

from StackClass import ArrayStack
from TEST_CODE import *
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():
    
    testStack = ArrayStack()

    # TEST 1 - Test privacy
    # BEFORE TESTING: implement __init__, __is_empty()
    TEST_privacy(testStack)


    # TEST 2 - Test stack creation
    # BEFORE TESTING: implement __len__, __str__
    TEST_new_stack(testStack)
    

    # TEST 3 - Test push
    # BEFORE TESTING: implement .push()
    TEST_push(testStack)


    # TEST 4 - Test pop
    # BEFORE TESTING: implement .pop()
    TEST_pop(testStack)


    # TEST 5 - Test top
    # BEFORE TESTING: implement .top()
    TEST_top(testStack)


    # TEST 6 - Test docstrings
    # BEFORE TESTING: implement all methods & docstrings
    TEST_docs(testStack)




if __name__ == "__main__":
    os.system("clear")
    main()