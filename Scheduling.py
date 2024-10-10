class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time

def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

def srtf(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]
        if not available_processes:
            current_time = processes[0].arrival_time
            continue
        process = min(available_processes, key=lambda x: x.remaining_time)
        processes.remove(process)
        if process.remaining_time > 1:
            current_time += 1
            process.remaining_time -= 1
            processes.append(process)
        else:
            current_time += process.remaining_time
            process.waiting_time = current_time - process.arrival_time - process.burst_time
            process.turnaround_time = process.waiting_time + process.burst_time

def priority_non_preemptive(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

def priority_preemptive(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]
        if not available_processes:
            current_time = processes[0].arrival_time
            continue
        process = min(available_processes, key=lambda x: x.priority)
        processes.remove(process)
        if process.remaining_time > 1:
            current_time += 1
            process.remaining_time -= 1
            processes.append(process)
        else:
            current_time += process.remaining_time
            process.waiting_time = current_time - process.arrival_time - process.burst_time
            process.turnaround_time = process.waiting_time + process.burst_time

def round_robin(processes, quantum):
    queue = processes[:]
    current_time = 0
    while queue:
        process = queue.pop(0)
        if process.burst_time > quantum:
            current_time += quantum
            process.burst_time -= quantum
            queue.append(process)
        else:
            current_time += process.burst_time
            process.waiting_time = current_time - process.arrival_time - process.burst_time
            process.turnaround_time = process.waiting_time + process.burst_time