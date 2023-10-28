import os
import sys
import threading
import time
import logging
from queue import Queue

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class Process:
    def __init__(self, name):
        self.name = name
        self.pid = None
        self.threads = []
        self.message_queue = Queue()
        self.lock = threading.Lock()  # Mutex (Lock) for process-level synchronization

class Thread:
    def __init__(self, name):
        self.name = name
        self.thread = None

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.lock = threading.Lock()

    def create_process(self, name):
        with self.lock:
            pid = os.fork()
            if pid == 0:
                # Child process
                logging.info(f"Child process {name} (PID: {os.getpid()}) created.")  # Simulate process execution
                sys.exit()
            else:
                self.processes[pid] = Process(name)
                self.processes[pid].pid = pid
                logging.info(f"Parent process created child {name} with PID: {pid}.")

    def list_processes(self):
        with self.lock:
            logging.info("List of running processes:")
            for pid, process in self.processes.items():
                logging.info(f"PID: {pid}, Name: {process.name}")

    def terminate_process(self, pid):
        with self.lock:
            if pid in self.processes:
                os.kill(pid, 9)  # Kill the process
                del self.processes[pid]
                logging.info(f"Process with PID {pid} terminated.")
            else:
                logging.error(f"Process with PID {pid} not found.")

    def create_thread(self, process_pid, thread_name):
        with self.lock:
            if process_pid in self.processes:
                process = self.processes[process_pid]
                thread = Thread(thread_name)
                thread.thread = threading.Thread(target=self.thread_function, args=(thread.name,))
                process.threads.append(thread)
                thread.thread.start()
                logging.info(f"Thread {thread.name} created in process {process.name} (PID: {process_pid}).")

    def thread_function(self, thread_name):
        logging.info(f"Thread {thread_name} started.")
        command = input("Enter a command (create/list/terminate/create_thread/send_message/receive_messages/exit): ")
        if command == "create":
            name = input("Enter the process name: ")
            self.create_process(name)
        elif command == "list":
            self.list_processes()
        elif command == "terminate":
            pid = int(input("Enter the PID of the process to terminate: "))
            self.terminate_process(pid)
        elif command == "create_thread":
            pid = int(input("Enter the PID of the process to create a thread in: "))
            thread_name = input("Enter the thread name: ")
            self.create_thread(pid, thread_name)
        elif command == "send_message":
            source_pid = int(input("Enter the source PID: "))
            target_pid = int(input("Enter the target PID: "))
            message = input("Enter the message: ")
            self.send_message(source_pid, target_pid, message)
        elif command == "receive_messages":
            pid = int(input("Enter the PID to receive messages: "))
            self.receive_messages(pid)
        elif command == "exit":
            logging.info("Exiting the Process Manager.")
            sys.exit()
        else:
            logging.error("Invalid command. Please try again.")

        logging.info(f"Thread {thread_name} finished.")

    def send_message(self, source_pid, target_pid, message):
        if source_pid in self.processes and target_pid in self.processes:
            source_process = self.processes[source_pid]
            target_process = self.processes[target_pid]
            with target_process.lock:  # Mutex (Lock) for process-level synchronization
                target_process.message_queue.put(f"From {source_process.name}: {message}")
        else:
            logging.error("Invalid source or target PID.")

    def receive_messages(self, pid):
        if pid in self.processes:
            process = self.processes[pid]
            while not process.message_queue.empty():
                message = process.message_queue.get()
                logging.info(f"Process {process.name} received message: {message}")
        else:
            logging.error("Invalid PID.")

if __name__ == "__main__":
    process_manager = ProcessManager()

    while True:
        command = input("Enter a command (create/list/terminate/create_thread/send_message/receive_messages/exit): ")
        if command == "create":
            name = input("Enter the process name: ")
            process_manager.create_process(name)
        elif command == "list":
            process_manager.list_processes()
        elif command == "terminate":
            pid = int(input("Enter the PID of the process to terminate: "))
            process_manager.terminate_process(pid)
        elif command == "create_thread":
            pid = int(input("Enter the PID of the process to create a thread in: "))
            thread_name = input("Enter the thread name: ")
            process_manager.create_thread(pid, thread_name)
        elif command == "send_message":
            source_pid = int(input("Enter the source PID: "))
            target_pid = int(input("Enter the target PID: "))
            message = input("Enter the message: ")
            process_manager.send_message(source_pid, target_pid, message)
        elif command == "receive_messages":
            pid = int(input("Enter the PID to receive messages: "))
            process_manager.receive_messages(pid)
        elif command == "exit":
            logging.info("Exiting the Process Manager.")
            sys.exit()
        else:
            logging.error("Invalid command. Please try again.")
