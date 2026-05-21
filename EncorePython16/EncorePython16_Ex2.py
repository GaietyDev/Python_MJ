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
    max_duration = int(input("Enter the maximum sleep duration in seconds: "))

    thread = SleepThread("Thread-1", max_duration)
    thread.start()

if __name__ == "__main__":
    main()
# AI Generated Code
