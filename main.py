class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next


class Stack:
  def __init__(self):
    self.topItem = None

  def push (self, value):
    Item = Node(value, self.topItem)
    self.topItem = Item

  def pop (self) -> str:
    if self.topItem is None:
      # print("Error: Stack is empty")
      return ""

    object, result = self.topItem, self.topItem.value
    self.topItem = self.topItem.next

    del object

    return result

  def __str__(self) -> str:
    if self.topItem is None:
      # print("Warning: Stack is empty")
      return ""

    result = self.topItem.value
    currentItem = self.topItem
    while currentItem.next is not None:
      currentItem = currentItem.next
      result += currentItem.value

    return result


class Equation:
  def __init__(self, strEquation):
    self.equation = strEquation
    self.Stack = Stack()
    
  def __precedence (self, strOperator) -> int:
    if strOperator == "(" or strOperator == ")":
      return -1 #ASLJDSA
    if strOperator == "^":
      return 3
    elif strOperator == "*" or strOperator == "/":
      return 2
    elif strOperator == "+" or strOperator == "-":
      return 1
    else:
      return 0

  def __infix_to_postFix(self) -> str:
    infix = self.equation
    postfix = ""
    stack = Stack()

    for i in range(len(infix)):
      # print("Postfix: ", postfix)
      # print("Stack: ", stack)
      if infix[i] == ")":
        while stack.topItem and stack.topItem.value != "(":
          postfix += stack.pop()

        stack.pop()
        continue
      elif infix[i] == "(":
        stack.push(infix[i])
      elif infix[i].isalpha():
        postfix += infix[i]
      else:
        while stack.topItem and self.__precedence(stack.topItem.value) >= self.__precedence(infix[i]):
          postfix += stack.pop()
          
        stack.push(infix[i])

    while stack.topItem:
      postfix += stack.pop()
    # for i in range(len(infix)):
    #   if infix[i].isdigit():
    #     postfix += infix[i]
    #   elif infix[i] == "(":
    #     stack.push(infix[i])
    #   elif infix[i] == ")":
    #     while stack.topItem is not None and stack.topItem.value != "(":
    #       postfix += stack.pop()
    #     stack.pop()
    #   else:
    #     while stack.topItem is not None and self.__precedence(infix[i]) <= self.__precedence(stack.topItem.value):
    #       postfix += stack.pop()
          
    #     stack.push(infix[i])
        
    # while stack.topItem is not None:
    #   postfix += stack.pop()
      
    return postfix

  def __infix_to_prefix(self) -> str:
    # return ""
    return self.__infix_to_postFix()[::-1]

    
  def __postfix_to_infix(self) -> str:
    stack = Stack()
    postFix = self.get_postfix()
    
    while len(postFix) > 0:
      if postFix[0] not in ['*','/','+','-']:
        stack.push(postFix[0])
  
      else:
        a, b = stack.pop(), stack.pop()
        stack.push(b + postFix[0] + a)
  
      postFix = postFix[1:]

    result = str(stack)
    del stack
    return result

  def __postfix_to_prefix(self) -> str:
    stack = Stack()
    prefix = self.get_prefix()
    
    while len(prefix) > 0:
      if prefix[0] not in ['*','/','+','-']:
        stack.push(prefix[0])
        
      else:
        a, b = stack.pop(), stack.pop()
        stack.push(prefix[0] + b + a)
        
      prefix = prefix[1:]
      
    result = str(stack)
    del stack
    return result

  def get_postfix(self) -> str:
    postFix = self.__infix_to_postFix()
    return postFix

  def get_prefix(self) -> str:
    prefix = self.__infix_to_prefix()
    return prefix

  

# Test the Equation class
# equation = Equation('2*(3+4)')
# print('Infix:', equation.equation)
# print('Postfix:', equation.get_postfix())
# print('Prefix:', equation.get_prefix())
equation = Equation('(a+b)*(c+d)')
print('Infix:', equation.equation)
print('Postfix:', equation.get_postfix())
print('Prefix:', equation.get_prefix())
print('')

equation = Equation('a+b+c+d')
print('Infix:', equation.equation)
print('Postfix:', equation.get_postfix())
print('Prefix:', equation.get_prefix())
print('')

equation = Equation('a*(b+c)*d')
print('Infix:', equation.equation)
print('Postfix:', equation.get_postfix())
print('Prefix:', equation.get_prefix())
