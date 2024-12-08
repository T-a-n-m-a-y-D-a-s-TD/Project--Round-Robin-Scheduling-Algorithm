# Operating Systems (OS)

# Round-Robin-Simulation

Overview
This project implements the Round Robin Scheduling Algorithm for CPU scheduling. It simulates the scheduling of processes with specific burst times and arrival times, calculates their Turnaround Time (TAT) and Waiting Time (WT), and generates a Gantt chart to visualize the scheduling order. The application is built using Python and the Streamlit library.

Features
Simulates the Round Robin scheduling algorithm.
Calculates Average Turnaround Time (TAT) and Average Waiting Time (WT).
Generates a Gantt chart to visualize the process execution.
Easy-to-use interface with inputs via Streamlit.
Table of Contents
Introduction
Problem Statement
Objectives
Methodology
Installation
Introduction
Round Robin (RR) is a preemptive scheduling algorithm used in Operating Systems for CPU scheduling. It allocates each process a fixed time quantum for execution. If a process does not finish within its time quantum, it is preempted and placed at the end of the queue.

This project simulates the Round Robin scheduling algorithm with user input and calculates the turnaround time and waiting time for each process. It also visualizes the execution order using a Gantt chart.

Problem Statement
Given the following processes with their burst times and arrival times:

    Process ID	   Burst Time (ms)	   Arrival Time (ms)
       P1	             10	                  0
       P2	              5	                  1
       P3	              8	                  2
       

Time Quantum (TQ) = 3 ms
The algorithm will simulate the scheduling, calculate the Turnaround Time (TAT) and Waiting Time (WT) for each process, and generate a Gantt chart to represent the scheduling order.

Objectives
Simulate the Round Robin Scheduling algorithm.
Calculate Turnaround Time and Waiting Time.
Generate a Gantt chart to represent process execution.
Display average turnaround and waiting times.
Methodology
Input Data: The user provides the number of processes, burst times, and arrival times via Streamlit input fields.
Execution Simulation:
The Round Robin algorithm allocates CPU time in fixed time quanta to each process in a circular order.
Processes are preempted if their burst time exceeds the quantum and are placed back into the queue.
Time Calculations:
Turnaround Time (TAT): ( TAT = Completion Time - Arrival Time )
Waiting Time (WT): ( WT = TAT - Burst Time )
Results Visualization: A Gantt chart is displayed to visualize the execution timeline.
