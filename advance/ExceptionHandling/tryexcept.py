
def forloopiterate():

  try:
       for i in ['a','b','c']:
         print(i**2)
  except:
      print("unsupported operand type(s) for ** or pow(): 'str' and 'int'")

forloopiterate()