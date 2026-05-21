from threading import Thread
import time
import random

class SleepThread(Thread):
    def __init__(self, name, max_duration):
        super().__init__(name=name)
        self.duration = random.randint(1, max_duration)

    def run(self):
        print(f"{self.name} sleeping for {self.duration} seconds")
        time.sleep(self.duration)
        print(f"{self.name} is waking up")

def main():
    # Input from the user
    num_threads = int(input("Enter the number of threads to create: "))
    max_duration = int(input("Enter the maximum sleep duration: "))

    # Create a list to hold thread objects
    threads = []

    # Instantiate threads
    for i in range(num_threads):
        thread = SleepThread(f"Thread-{i + 1}", max_duration)
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

if __name__ == "__main__":
    main()
# AI Generated Code
