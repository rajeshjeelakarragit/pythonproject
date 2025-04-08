import multiprocessing


def increment(shared_counter, lock):
    with lock:
        shared_counter.value += 1
        print(f"Counter: {shared_counter.value}")


if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)  # Shared integer
    lock = multiprocessing.Lock()

    processes = [multiprocessing.Process(target=increment, args=(counter, lock)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Final Counter Value: {counter.value}")

"""
Counter: 1
Counter: 2
Counter: 3
Counter: 4
Counter: 5
Final Counter Value: 5
"""