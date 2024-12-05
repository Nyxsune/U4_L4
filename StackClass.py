"""
Connor Cox
U4 L1
Stack
"""

class ArrayStack:

  def __init__(self):
    self.__stack = []
    self.__size = 0

  def push(self, item):
    """Adds an item to the top of the stack"""
    self.__stack.append(item)
    self.__size += 1

  def pop(self):
    """Removes top of stack and returns what was removed"""
    empty = self.__is_empty()
    if empty:
      raise IndexError("stack is empty")
    else:
      last = str(self.__stack[-1])
      del self.__stack[-1]
      self.__size -= 1
      return last
    
  
  def top(self):
    """Checks the top of the stack"""
    empty = self.__is_empty()
    if empty:
      raise IndexError("stack is empty")
    else:
      return self.__stack[-1]

  def __len__(self):
    """Returns size of stack"""
    return self.__size

  def __is_empty(self):
    if self.__size == 0:
      return True
    else:
      return False

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out