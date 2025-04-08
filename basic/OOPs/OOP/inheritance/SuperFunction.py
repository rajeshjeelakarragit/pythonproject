# parent class
class ParentDemo:
   def __init__(self, msg):
      self.message = msg

   def showMessage(self):
      print(self.message)

# child class
class ChildDemo(ParentDemo):
   def __init__(self, msg):
      # use of super function
      super().__init__(msg)

# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
obj.showMessage()