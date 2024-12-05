##### Global color variables #####
from colorama import Fore
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''
##################################

def TEST_privacy(stackobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Privacy{W}\n")

    try:
        print(stackobj.stack)
        print(f"{W}Stack array is private: {R}FAILED{W}")
    except:
        print(f"{W}Stack array is private: {G}PASSED{W}")
    
    try:
        print(stackobj.size)
        print(f"{W}Stack size is private: {R}FAILED{W}")
    except:
        print(f"{W}Stack size is private: {G}PASSED{W}")

    try:
        print(stackobj.is_empty())
        print(f"{W}is_empty() is private: {R}FAILED{W}")
    except:
        print(f"{W}is_empty() is private: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_new_stack(stackobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Stack Creation{W}\n")

    print(f"{B}Initial Stack: {stackobj}{W}\n")

    test = len(stackobj) == 0
    if test: 
        print(f"Initial stack contains ZERO elements: {G}PASSED{W}")
    else:
        print(f"Initial stack contains ZERO elements: {R}FAILED{W}")

    test = str(stackobj) == '<TOP'
    if test: 
        print(f"Correct to-string method: {G}PASSED{W}")
    else:
        print(f"Correct to-string method: {R}FAILED{W}")

    


def TEST_push(stackobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Push{W}\n")

    stackobj.push("A")
    test1 = stack_to_list(str(stackobj))[-1] == 'A'
    stackobj.push("B")
    test2 = stack_to_list(str(stackobj))[-1] == 'B'
    stackobj.push("C")
    test3 = stack_to_list(str(stackobj))[-1] == 'C'

    print(f"{B}Stack of 3 elements: {stackobj}{W}\n")

    test = test1 and test2 and test3
    if test: 
        print(f"Elements added to top: {G}PASSED{W}")
    else:
        print(f"Elements added to top: {R}FAILED{W}")

    
    test = len(stackobj) == 3
    if test: 
        print(f"Push affects size: {G}PASSED{W}")
    else:
        print(f"Push affects size: {R}FAILED{W}")

    print("~" * 50, "\n\n")


def TEST_pop(stackobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Pop{W}\n")

    print(f"{B}Initial Stack: {stackobj}    {len(stackobj)} elements{W}\n")

    ele = stackobj.pop()

    test = ele == "C"
    if test: 
        print(f"Pop returns a value: {G}PASSED{W}")
    else:
        print(f"Pop returns a value: {R}FAILED{W}")

    test = stack_to_list(str(stackobj))[-1] == 'B'
    if test: 
        print(f"Pop removes top of stack: {G}PASSED{W}")
    else:
        print(f"Pop removes top of stack: {R}FAILED{W}")

    test = len(stackobj) == 2
    if test: 
        print(f"Pop affects size: {G}PASSED{W}")
    else:
        print(f"Pop affects size: {R}FAILED{W}")

    print(f"\n{B}Updated Stack: {stackobj}    {len(stackobj)} elements{W}\n")

    ele = stackobj.pop()
    ele = stackobj.pop()

    try:
        ele = stackobj.pop()
        print(f"Pop from an empty stack raises exception: {R}FAILED{W}")
    except:
        print(f"Pop from an empty stack raises exception: {G}PASSED{W}")

    print(f"\n{B}Resulting Stack: {stackobj}    {len(stackobj)} elements{W}")

    print("~" * 50, "\n\n")


def TEST_top(stackobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Top{W}\n")

    stackobj.push("W")
    stackobj.push("X")
    stackobj.push("Y")
    stackobj.push("Z")

    print(f"{B}Initial Stack: {stackobj}    {len(stackobj)} elements{W}\n")

    ele = stackobj.top()

    test = ele == "Z"
    if test: 
        print(f"Top returns a value: {G}PASSED{W}")
    else:
        print(f"Top returns a value: {R}FAILED{W}")

    test = stack_to_list(str(stackobj))[-1] == 'Z'
    if test: 
        print(f"Top does not change stack: {G}PASSED{W}")
    else:
        print(f"Top does not change stack: {R}FAILED{W}")

    test = len(stackobj) == 4
    if test: 
        print(f"Top does not affect size: {G}PASSED{W}")
    else:
        print(f"Top does not affect size: {R}FAILED{W}")
    
    for i in range(4):
        stackobj.pop()

    try:
        ele = stackobj.top()
        print(f"Top from an empty stack raises exception: {R}FAILED{W}")
    except:
        print(f"Top from an empty stack raises exception: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_docs(stackobj):

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")
    

    doc = stackobj.push.__doc__
    if doc != None:
        print(f"{B}Push Documentation:{W} {doc}\n")
    else:
        print(f"{R}Push Documentation Missing{W}\n")

    doc = stackobj.pop.__doc__
    if doc != None:
        print(f"{B}Pop Documentation:{W} {doc}\n")
    else:
        print(f"{R}Pop Documentation Missing{W}\n")

    doc = stackobj.top.__doc__
    if doc != None:
        print(f"{B}Top Documentation:{W} {doc}\n")
    else:
        print(f"{R}Top Documentation Missing{W}\n")

    doc = stackobj.__len__.__doc__
    if doc != None:
        print(f"{B}Len Documentation:{W} {doc}\n")
    else:
        print(f"{R}Len Documentation Missing{W}\n")

    doc = stackobj.__str__.__doc__
    if doc != None:
        print(f"{B}Str Documentation:{W} {doc}\n")
    else:
        print(f"{R}Str Documentation Missing{W}\n")

    print("~" * 50, "\n\n")



##################################
#        Helper Functions        #
##################################

def stack_to_list(stackstr):
    out = stackstr.split(" ")
    del out[-1]
    return out