import time
from typing import override
from contextlib import AbstractContextManager


def message_closure(message):
    def printer():
        print(f"[Closure] Message is: {message}")
    return printer


my_closure = message_closure("Hello from the closure!")
my_closure()


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        print(f"[Decorator] Running function: {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[Decorator] Execution time of '{func.__name__}': {execution_time:.4f} seconds")
        return result
    return wrapper



class FileWriter(AbstractContextManager):
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None

    @override
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    @override
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"[Context Manager] File '{self.filename}' closed successfully.")


def write_log_to_file(filename, data):
    with FileWriter(filename, 'w') as file:
        file.write(data)
        print(f"[Context Manager] Data written to '{filename}' successfully.")


@measure_execution_time
def long_running_task():
    print("[Function] Starting a time-consuming task...")
    time.sleep(2)
    print("[Function] Task completed.")
    return "Task Result"


if __name__ == "__main__":
    result = long_running_task()
    log_message = f"Result of the task: {result}\n"
    write_log_to_file("execution_log.txt", log_message)
