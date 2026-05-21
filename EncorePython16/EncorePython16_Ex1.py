from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(self.name)

# Create and start the thread
thread = MyThread("My First Thread")
thread.start()
# AI Generated Code
