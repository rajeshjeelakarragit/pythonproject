def new_dec(orig_func):

    def wrap_func():
        print("hello rajesh start ")
        orig_func()
        print("hello rajesg end")
    return wrap_func


@new_dec
def hello():
    print("Hello")

hello()

'''
hello rajesh start 
hello
hello rajesg end
'''

def new_dec(orig_func):

    def wrap_func():
        print("Some extra code, before original function is calling")
        orig_func()
        print("Some extra code, after original function is calling")
    return wrap_func

#@new_dec
def func_need_dec():
      print("I want to be decor")

#dec_func = new_dec(func_need_dec)

#dec_func()

#func_need_dec()

###########################################
def newfunc(or_func):

    print("new funcs")
    or_func()


#@newfunc
def orininfal_func():
    print("this is original func")

#orininfal_func()

#newfunc(orininfal_func)

