# Project Report

## By: Mitkumar Patel

#### Advanced Process Manager with Process Synchronization


### INTRODUCTION

The primary objective of this project is to design and implement an advanced Process Manager
that not only empowers users to create, manage, and synchronize processes but also offers a
comprehensive set of features to facilitate robust inter-process communication (IPC) and
synchronization between threads. This Process Manager is designed to provide a unified and
user-friendly interface for process creation, management, and synchronization, harnessing the
capabilities of system calls for process and thread control. It stands as an embodiment of
ingenuity in the domain of
multi-processing, striving to enhance the performance and stability of diverse applications.

### Objectives

The objectives of lab are:

1. To manipulate processes and threads in many different aspects.
2. To exploit system calls to manipulate processes and threads.
3. To develop a software which operates reliably with reducing conflicts in using
    system resources.

### System Requirements:

```
Following are the system requirements of the application:
```
```
● Unix/Linux operating system (tested and programmed on Ubuntu 20)
● Python 3
```
### Installation And Usage:

```
Following are the installation and usage instruction:
```
```
● To run this application, first you need the Unix/Linux operating system and then you
need to install python3 using the Unix/Linux command in the terminal as : sudo apt-
get install python3.
● To run the program in terminal, navigate to the folder using cd command and run
the program using python by command as: python3 Process-Manager.py.
● Type the name of functionality given to you by the program which you want to use.
```

### Functionalities:

## ❖ Process Creation

#### Introduction:

```
The system allows users to create new processes, harnessing system calls
such as “ fork “ and ” exec ” This mechanism is fundamental for running
multiple tasks concurrently, which is essential in scenarios ranging from
server-side applications to parallel computing.
```
#### Code with explanation:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/7e516f45-1017-434e-9e45-eda75ead6cf0)



This code demonstrates the process creation functionality using fork. When you run it and
enter "create," it will create a child process, and you can verify this through the log output.

#### Output:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/612c7c15-f4ae-4ca4-b241-bac35c89fbd1)


## ❖ Process listing

#### Introduction:

The system allows users to list all processes. It shows the PID, Name and date on which
the process is created.

#### Code with explanation:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/4bc0f94e-6b5c-4d05-9eae-97b46bdc01fb)


```
This code demonstrates process management, allowing you to create and list processes.
Run the code, enter "create" to create a process, and enter "list" to list the running
processes.
```

#### Output:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/b1638368-8ee2-483f-9a31-4fb5f2a74931)



## ❖ Process Terminating

#### Introduction:

```
The system allows the user to terminate any processes that are created by the
user.
```
#### Code with explanation:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/ec2f603d-2d9a-44f5-9c00-f6f542e61132)


This code demonstrates process management, allowing you to create, list and terminate
processes. Run the code, enter "create" to create a process, and enter "list" to list the
running processes and terminate to kill the process by providing it PID.


#### Output:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/29f7031a-549a-40c6-86d9-549bed9cb7fd)



## ❖ Thread Support:

#### Introduction:

```
It leverages system calls like “pthread_create “and synchronization
primitives to enhance parallel execution, providing a solid foundation for
multi-threaded applications..
```
#### Code with explanation:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/5b3228fc-e847-451a-b8a6-41b4681a8bde)


This code demonstrates the threading functionality, allowing you to create thread to run
multiple processes side by side


## ❖ IPC Functionality:

#### Introduction:

```
Inter-Process Communication (IPC) allows processes to communicate and
share data. One common method for IPC is using pipes.
```
#### Code with explanation:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/9efdbdc6-0cc3-47d9-ad23-ad8efba5fccd)


This code demonstrates the Inter-Process Communication (IPC) functionality, allowing
processes to send and receive messages from one another and communicate with each
other.

#### Output:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/6c878980-3a95-4840-93b0-c56c3e5f6841)


## ❖ Process Synchronization:

#### Introduction:

```
Process synchronization is a critical aspect of multi-process
programming and it helps ensure that processes or threads work together in
a coordinated and orderly manner. Common synchronization mechanisms
include locks, semaphores, and condition variables.
```
#### Example Code with explanation:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/3982a95c-3f13-4ca1-b96c-8f1892f75ff6)


Here, I have provided an example of using locks (mutex) for process
synchronization within the Process Manager project. In this code, we have two
processes: the producer and the consumer. The producer produces items and adds them to
a shared buffer, while the consumer consumes items from the buffer. To ensure that the
producer and consumer do not access the buffer simultaneously, a lock is used to
synchronize access.


### Complete Code:
'''

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
'''

### Output:
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/3a6e26bb-7239-4290-a363-ac6c6911000a)
![image](https://github.com/patelmit101/cmpsc472project1/assets/62670195/fc1e7acd-f5cb-47f6-ab77-f7832fb43a34)


### Output Explanation:

```
● After running the process manager, I created 3 processes: test1,test2 and test3 to show
the functionality of the creating process. The output of each command is well organized
and easy to understand and gives logs and reports on each command execution.
● After that I list all the processes using the “list” command and then terminate the test
process using the terminate command.
● Then, I create the thread using the “create_thread” command and name it as; thread1.
After creating the thread1, again a menu of processes manager appears which shows
that the thread is running as a separate process. In the thread function, I have provided
the function to use the functionalities of the process manager so that we should have
access to process manager functionalities in this separate thread. We used to create
functionality to create process thread1process and we see in the output that new
process thread1process is created and then thread1 finished.
● Then, I tested the IPC functionality by sending a message “hello” from process test
to test2 by using send_messages and receiving the message by process test2 using
receive_messages.
● The “exit” command closes the program.
```

