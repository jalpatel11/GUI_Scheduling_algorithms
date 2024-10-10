import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Scheduling import Process, fcfs, sjf, srtf, priority_non_preemptive, priority_preemptive, round_robin
from datetime import datetime

def draw_gantt_chart(processes, title):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    
    y_labels = []
    for i, process in enumerate(processes):
        start_time = process.arrival_time + process.waiting_time
        ax.broken_barh([(start_time, process.burst_time)], (i * 10, 9), facecolors=('tab:blue'))
        y_labels.append(f"P{process.pid}")
    
    ax.set_yticks([i * 10 + 5 for i in range(len(processes))])
    ax.set_yticklabels(y_labels)
    st.pyplot(fig)

# Title and header
# st.title("CPU Scheduling Algorithms")
st.markdown('<h1 class="big-font">CPU Scheduling Algorithms</h1>', unsafe_allow_html=True)
year=datetime.now().year
st.markdown("""
    **Author:** Jal Patel  
    **GitHub:** [jalpatel11](https://github.com/jalpatel11)  
""")

st.markdown("""
### Instructions to Use the App

**Add Processes:**
- Use the sidebar to input the process details (PID, Arrival Time, Burst Time, and Priority if applicable).
- Click the "Add Process" button to add the process to the list.

**Select Scheduling Algorithm:**
- Use the dropdown menu to select the desired scheduling algorithm (FCFS, SJF, SRTF, Priority (Non-preemptive), Priority (Preemptive), or Round Robin).
- If you select Round Robin, you will need to input the quantum time.

**Run the Algorithm:**
- Click the "Run" button to execute the selected scheduling algorithm.
- The Gantt chart and results (Waiting Time and Turnaround Time for each process) will be displayed.

**View Results:**
- The processes and their details will be displayed in a table.
- The Gantt chart will visualize the scheduling.
- The results table will show the Waiting Time and Turnaround Time for each process.
""")

# Select scheduling algorithm
algorithm = st.selectbox("Select Scheduling Algorithm", ["FCFS", "SJF", "SRTF", "Priority (Non-preemptive)", "Priority (Preemptive)", "Round Robin"])

# Input form for processes
st.sidebar.header("Add Process")
pid = st.sidebar.number_input("PID", min_value=1, step=1)
arrival_time = st.sidebar.number_input("Arrival Time", min_value=0, step=1)
burst_time = st.sidebar.number_input("Burst Time", min_value=1, step=1)
priority = 0
if algorithm in ["Priority (Non-preemptive)", "Priority (Preemptive)"]:
    priority = st.sidebar.number_input("Priority", min_value=0, step=1)

if st.sidebar.button("Add Process"):
    if 'processes' not in st.session_state:
        st.session_state.processes = []
    st.session_state.processes.append(Process(pid, arrival_time, burst_time, priority))

# Display added processes in a table
if 'processes' in st.session_state:
    st.write("### Processes")
    process_data = []
    for process in st.session_state.processes:
        if algorithm in ["FCFS", "SJF", "SRTF"]:
            process_data.append({
                "PID": process.pid,
                "Arrival Time": process.arrival_time,
                "Burst Time": process.burst_time
            })
        else:
            process_data.append({
                "PID": process.pid,
                "Arrival Time": process.arrival_time,
                "Burst Time": process.burst_time,
                "Priority": process.priority
            })
    df = pd.DataFrame(process_data)
    st.table(df)

# Quantum input for Round Robin
quantum = 0
if algorithm == "Round Robin":
    quantum = st.number_input("Quantum", min_value=1, step=1)

# Run selected algorithm
if st.button("Run"):
    processes_copy = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in st.session_state.processes]
    
    if algorithm == "FCFS":
        fcfs(processes_copy)
        title = "First-Come, First-Served (FCFS)"
    elif algorithm == "SJF":
        sjf(processes_copy)
        title = "Shortest Job First (SJF)"
    elif algorithm == "SRTF":
        srtf(processes_copy)
        title = "Shortest Remaining Time First (SRTF)"
    elif algorithm == "Priority (Non-preemptive)":
        priority_non_preemptive(processes_copy)
        title = "Priority Scheduling (Non-preemptive)"
    elif algorithm == "Priority (Preemptive)":
        priority_preemptive(processes_copy)
        title = "Priority Scheduling (Preemptive)"
    elif algorithm == "Round Robin":
        round_robin(processes_copy, quantum)
        title = "Round Robin (RR)"
    
    draw_gantt_chart(processes_copy, title)
    
    st.write("### Results")
    result_data = []
    for process in processes_copy:
        result_data.append({
            "PID": process.pid,
            "Waiting Time": process.waiting_time,
            "Turnaround Time": process.turnaround_time
        })
    result_df = pd.DataFrame(result_data)
    st.table(result_df)

# Footer
st.markdown("""
    **© 2024 Jal Patel. All rights reserved.**
""")
