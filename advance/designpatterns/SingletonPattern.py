
"""
The Singleton pattern ensures a class has only one instance and provides a global point of access to it.
"""
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        #cls._instance = None
        print(cls._instance)
        if cls._instance is None:
            print("None")
        else:
            print("Not None")

        if cls._instance is not None:
            print("None")
        else:
            print("Not None")

        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
