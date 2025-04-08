import multiprocessing

def print_square(number):
    print(f"Square of {number}: {number * number}")

if __name__ == "__main__":
    process = multiprocessing.Process(target=print_square, args=(5,))
    process.start()
    process.join()

"""
Square of 5: 25

"""