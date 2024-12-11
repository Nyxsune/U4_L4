"""
Connor Cox
U4 Lab 4
balanced brackets
"""
from StackClass import ArrayStack

def first_check(line):
    line = list(line)
    stack = ArrayStack()
    brackets = {
        "curly":0,
        "square":0,
        "normal":0
    }
    isBalanced = False

    for item in line:
        if item == "{" or item == "}":
            brackets["curly"] += 1
        elif item == "[" or item == "]":
            brackets["square"] += 1
        elif item == "(" or item == ")":
            brackets["normal"] += 1
        stack.push(item)
    
    if brackets["curly"]%2 == 0 and brackets["square"]%2 == 0 and brackets["normal"]%2 == 0:
        isBalanced = True

    return isBalanced, stack

def second_check(stack):
    #I know it looks quirky, but I was literally about to have a breakdown over making this work, so this is what you get
    normNum = 0
    curlNum = 0
    sqrNum = 0
    index = 0
    brackets = {}
    for i in range(len(stack)):
        bracket = stack.pop()
        if bracket == "]":
            sqrNum += 1
            key = "Square" + str(sqrNum)
            brackets[key] = index

        elif bracket == ")":
            normNum += 1
            key = "Normal" + str(normNum)
            brackets[key] = index

        elif bracket == "}":
            curlNum += 1
            key = "Curly" + str(curlNum)
            brackets[key] = index
        
        elif bracket == "[":
            key = "Square" + str(sqrNum)
            distance = index - brackets[key]
            del brackets[key]
            if distance % 2 == 0:
                isBalanced = False
                break
            else:
                isBalanced = True
            sqrNum -= 1

        elif bracket == "(":
            key = "Normal" + str(normNum)
            distance = index - brackets[key]
            del brackets[key]
            if distance % 2 == 0:
                isBalanced = False
                break
            else:
                isBalanced = True
            normNum -= 1

        elif bracket == "{":
            key = "Curly" + str(curlNum)
            distance = index - brackets[key]
            del brackets[key]
            if distance % 2 == 0:
                isBalanced = False
                break
            else:
                isBalanced = True
            curlNum -= 1
        index += 1
    
    return isBalanced

def balanced(line):
    isBalanced, stack = first_check(line)

    if isBalanced:
        isBalanced = second_check(stack)

    return isBalanced

def main():
    test1 = "()(()){([()])}"
    test2 = "((()(()){([()])}))"
    test3 = ")(()){([()])]"
    test4 = "({[])}"
    test5 = "("

    for test in [test1, test2, test3, test4, test5]:
        isBalanced = balanced(test)
        if isBalanced:
            isBalanced = "Balanced"
        else:
            isBalanced = "Unbalanced"
        print(f"{test} - {isBalanced}")


if __name__ == "__main__":
    main()