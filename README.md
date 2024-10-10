

# CPU Scheduling Algorithms Visualization

This Streamlit app visualizes various CPU scheduling algorithms including FCFS, SJF, SRTF, Priority (Non-preemptive), Priority (Preemptive), and Round Robin. The app allows users to input process details, select a scheduling algorithm, and view the results in a Gantt chart and table format.

## Features

- **Add Processes:** Input process details such as PID, Arrival Time, Burst Time, and Priority (if applicable).
- **Select Scheduling Algorithm:** Choose from FCFS, SJF, SRTF, Priority (Non-preemptive), Priority (Preemptive), or Round Robin.
- **Run the Algorithm:** Execute the selected scheduling algorithm and visualize the results.
- **View Results:** Display the processes, Gantt chart, and results table showing Waiting Time and Turnaround Time for each process.

## Deployed app can be viewed below...
[Click here](https://jalpatel11-gui-scheduling-algorithms-app-yfyzch.streamlit.app/)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jalpatel11/CPU-Scheduling-Algorithms.git
    cd CPU-Scheduling-Algorithms
    ```

2. Create a virtual environment:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to add processes and select a scheduling algorithm.

4. Click the "Run" button to execute the algorithm and view the results.

## File Structure

- `app.py`: Main application file for the Streamlit app.
- `Scheduling.py`: Contains the implementation of the scheduling algorithms.
- `requirements.txt`: List of required Python packages.
- `README.md`: This file.

## Scheduling Algorithms

- **FCFS (First-Come, First-Served):** Processes are executed in the order they arrive.
- **SJF (Shortest Job First):** Processes with the shortest burst time are executed first.
- **SRTF (Shortest Remaining Time First):** Preemptive version of SJF where the process with the shortest remaining burst time is executed next.
- **Priority (Non-preemptive):** Processes are executed based on priority, without preemption.
- **Priority (Preemptive):** Processes are executed based on priority, with preemption.
- **Round Robin:** Processes are executed in a cyclic order with a fixed time quantum.

## Author

**Jal Patel**  
**GitHub:** [jalpatel11](https://github.com/jalpatel11)

## License

This project is licensed under the MIT License.
