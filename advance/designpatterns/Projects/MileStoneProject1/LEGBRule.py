x=25

def printer():
    x=50
    return(x)

print(printer())

#GLOBAL
name = "THIS IS A GLOBAL STRING"

def greet():

    #ENCLOSING
    name= 'Sammy'
    def hello():
        #LOCAL
        name = 'i AM A LOCAL'
        print('Hello ' + name)

    hello()

greet()


namefirst = "THIS IS A GLOBAL STRING"

def greetGlobal():

    #ENCLOSING
   global  namefirst
   print(f"Hello this is global {namefirst}")
   def hello():
        #LOCAL
        namefirst = 'i AM A LOCAL'
        print('Hello ' + namefirst)
   hello()

greetGlobal()