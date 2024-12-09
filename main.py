"""
Connor Cox
U4 Lab 2
Reversal
"""
from StackClass import ArrayStack

def reverse(sentence):
    original = list(sentence)
    stack = ArrayStack()
    for char in original:
        stack.push(char)
    
    new = ""
    for i in range(len(stack)):
        new += stack.pop()
    
    return new


def main():
    original = "Sphinx of black quartz, judge my vow"
    reversed = reverse(original)
    print(f"Original: {original}\nReversed: {reversed}")

if __name__ == "__main__":
    main()