"""
Use threading.Lock to ensure only one thread accesses a resource at a time.

"""
import threading
lock = threading.Lock()

def safe_increment(counter):
    with lock:  # Acquire lock
        counter[0] += 1
        print(f"Counter incremented to {counter[0]} by {threading.current_thread().name}")

counter = [0]
threads = [threading.Thread(target=safe_increment, args=(counter,)) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Final Counter Value: {counter[0]}")


"""

Counter incremented to 1 by Thread-1 (safe_increment)
Counter incremented to 2 by Thread-2 (safe_increment)
Counter incremented to 3 by Thread-3 (safe_increment)
Counter incremented to 4 by Thread-4 (safe_increment)
Counter incremented to 5 by Thread-5 (safe_increment)
Final Counter Value: 5

"""