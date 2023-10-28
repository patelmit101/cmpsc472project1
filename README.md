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

This code demonstrates the process creation functionality using fork. When you run it and
enter "create," it will create a child process, and you can verify this through the log output.

#### Output:


## ❖ Process listing

#### Introduction:

The system allows users to list all processes. It shows the PID, Name and date on which
the process is created.

#### Code with explanation:

```
This code demonstrates process management, allowing you to create and list processes.
Run the code, enter "create" to create a process, and enter "list" to list the running
processes.
```

#### Output:


## ❖ Process Terminating

#### Introduction:

```
The system allows the user to terminate any processes that are created by the
user.
```
#### Code with explanation:

This code demonstrates process management, allowing you to create, list and terminate
processes. Run the code, enter "create" to create a process, and enter "list" to list the
running processes and terminate to kill the process by providing it PID.


#### Output:


## ❖ Thread Support:

#### Introduction:

```
It leverages system calls like “pthread_create “and synchronization
primitives to enhance parallel execution, providing a solid foundation for
multi-threaded applications..
```
#### Code with explanation:

This code demonstrates the threading functionality, allowing you to create thread to run
multiple processes side by side

#### Output:


## ❖ IPC Functionality:

#### Introduction:

```
Inter-Process Communication (IPC) allows processes to communicate and
share data. One common method for IPC is using pipes.
```
#### Code with explanation:

This code demonstrates the Inter-Process Communication (IPC) functionality, allowing
processes to send and receive messages from one another and communicate with each
other.

#### Output:


## ❖ Process Synchronization:

#### Introduction:

```
Process synchronization is a critical aspect of multi-process
programming, and it helps ensure that processes or threads work together in
a coordinated and orderly manner. Common synchronization mechanisms
include locks, semaphores, and condition variables.
```
#### Example Code with explanation:

Here, I have provided an example of using locks (mutex) for process
synchronization within the Process Manager project. In this code, we have two
processes: the producer and the consumer. The producer produces items and adds them to
a shared buffer, while the consumer consumes items from the buffer. To ensure that the
producer and consumer do not access the buffer simultaneously, a lock is used to
synchronize access.


### Complete Code:



### Output:


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

