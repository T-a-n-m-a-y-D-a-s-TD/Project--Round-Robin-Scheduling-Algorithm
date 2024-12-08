import streamlit as st
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# Process class to hold each process' details
class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


# Function to calculate average waiting time and turnaround time
def calculate_avg_times(processes):
    total_turnaround_time = 0
    total_waiting_time = 0
    for process in processes:
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_waiting_time = total_waiting_time / len(processes)

    return avg_turnaround_time, avg_waiting_time


# Function to simulate Round Robin Scheduling
def round_robin(processes, time_quantum):
    # Initialize the processes
    queue = deque(processes)
    time = 0
    gantt_chart = []

    # Continue processing until all processes are completed
    while queue:
        process = queue.popleft()

        if process.remaining_time > time_quantum:
            gantt_chart.append((process.pid, time, time + time_quantum))
            process.remaining_time -= time_quantum
            time += time_quantum
            queue.append(process)  # Re-queue the process
        else:
            gantt_chart.append((process.pid, time, time + process.remaining_time))
            time += process.remaining_time
            process.completion_time = time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time

    # Calculate average turnaround time and waiting time
    avg_turnaround_time, avg_waiting_time = calculate_avg_times(processes)

    return gantt_chart, avg_turnaround_time, avg_waiting_time


# Streamlit UI
st.set_page_config(page_title="Round Robin Scheduling", page_icon=":guardsman:", layout="centered")

# Add a custom title with some styling
st.title("💻 Round Robin Scheduling Algorithm")

# Create a sidebar for better user experience
st.sidebar.header("Input Process Information")
num_processes = st.sidebar.number_input('Enter number of processes:', min_value=1, max_value=10, value=3)
time_quantum = st.sidebar.number_input('Enter time quantum (ms):', min_value=1, value=3)

# Getting process details (ID, Burst Time, Arrival Time)
processes = []
for i in range(num_processes):
    pid = st.sidebar.text_input(f'Enter Process ID for P{i + 1}:', value=f'P{i + 1}')
    burst_time = st.sidebar.number_input(f'Enter Burst Time for {pid}:', min_value=1, value=10)
    arrival_time = st.sidebar.number_input(f'Enter Arrival Time for {pid}:', min_value=0, value=0)
    processes.append(Process(pid, burst_time, arrival_time))

# Main content section for the simulation
st.markdown("### 🚀 Simulate Round Robin Scheduling")
st.write(
    "After inputting the processes and their burst times, press the button below to simulate the scheduling algorithm.")

# Button to start the simulation
if st.button('Simulate Round Robin'):
    # Run Round Robin algorithm
    gantt_chart, avg_turnaround_time, avg_waiting_time = round_robin(processes, time_quantum)

    # Display Gantt Chart in Streamlit text format
    st.markdown("### 📊 Gantt Chart:")
    gantt_data = [f"{pid} ({start}-{end})" for pid, start, end in gantt_chart]
    st.write(" | ".join(gantt_data))

    # Display Average Turnaround and Waiting Times
    st.markdown("### 🧮 Average Times:")
    st.write(f"Average Turnaround Time: {avg_turnaround_time:.2f} ms")
    st.write(f"Average Waiting Time: {avg_waiting_time:.2f} ms")

    # Plotting Gantt chart using Matplotlib
    fig, ax = plt.subplots(figsize=(12, 4))

    # Colors for each process (distinct colors for better clarity)
    colors = ['#FF6347', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2', '#FF1493', '#00FFFF', '#FFA500']

    # Plotting each process' bar in the Gantt chart
    current_time = 0
    for idx, (pid, start, end) in enumerate(gantt_chart):
        ax.barh(0, end - start, left=start, height=0.5, color=colors[idx % len(colors)], label=f'{pid} ({start}-{end})')

    ax.set_xlabel('Time (ms)', fontsize=12)
    ax.set_title('⏳ Gantt Chart for Round Robin Scheduling', fontsize=14)
    ax.set_xlim(0, max([end for _, _, end in gantt_chart]) + 5)  # Extend the time axis slightly for clarity
    ax.set_yticks([0])
    ax.set_yticklabels(['Processes'])

    # Add labels for each process
    for pid, start, end in gantt_chart:
        ax.text((start + end) / 2, 0, f'{pid}', ha='center', va='center', color='white', fontsize=10)

    # Add legend and grid for better readability
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)

    # Show the Gantt chart in Streamlit
    st.pyplot(fig)
