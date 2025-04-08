class GettersandSetterMethods:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age


   name = property(get_name, set_name, "name")
   age = property(get_age, set_age, "age")

e1=GettersandSetterMethods("Bhavana", 24)
print ("Name:", e1.get_name(), "age:", e1.get_age())
#e1.set_name("Archana")
#e1.set_age(21)
e1.name = "Archana"
e1.age = 23
print ("Name:", e1.get_name(), "age:", e1.get_age())