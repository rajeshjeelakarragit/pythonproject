import threading
import time

# Define a function for the thread
def print_numbers():
    for i in range(5):
        print(f"Thread {threading.current_thread().name} prints {i}")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_numbers, name="Thread-2")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads completed.")


"""

Thread Thread-1 prints 0
Thread Thread-2 prints 0
Thread Thread-2 prints 1
Thread Thread-1 prints 1
Thread Thread-2 prints 2
Thread Thread-1 prints 2
Thread Thread-2 prints 3
Thread Thread-1 prints 3
Thread Thread-2 prints 4
Thread Thread-1 prints 4
All threads completed.

"""
