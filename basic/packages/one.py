def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print("ONE.PY is being run directly")
    func()

else:
    print("ONE.PY has been imported")

"""
TOP LEVEL IN ONE.PY
ONE.PY is being run directly

"""