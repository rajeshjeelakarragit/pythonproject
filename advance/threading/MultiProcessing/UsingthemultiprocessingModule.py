import multiprocessing
import time


# Define a function to be executed by each process
def compute_square(number):
    print(f"Process {multiprocessing.current_process().name} computing square of {number}")
    time.sleep(1)
    return number * number


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a pool of workers
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(compute_square, numbers)

    print(f"Squares: {results}")


    """
Process SpawnPoolWorker-1 computing square of 1
Process SpawnPoolWorker-2 computing square of 2
Process SpawnPoolWorker-1 computing square of 3
Process SpawnPoolWorker-2 computing square of 4
Process SpawnPoolWorker-1 computing square of 5
Squares: [1, 4, 9, 16, 25]
    
    """