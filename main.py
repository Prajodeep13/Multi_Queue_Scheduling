from models.process import Process
from scheduling.assigner import assign_to_queues
from scheduling.round_robin import round_robin
from scheduling.fcfs import fcfs
from scheduling.sjf import sjf
from visualizer.gantt_chart import draw_gantt_chart

if __name__ == "__main__":
    # Sample process data
    processes = [
        Process("P1", 0, 10, 1),
        Process("P2", 2, 5, 2),
        Process("P3", 3, 7, 3),
        Process("P4", 4, 4, 1),
        Process("P5", 5, 3, 3)
    ]

    # Step 1: Assign to queues
    q1, q2, q3 = assign_to_queues(processes)

    # Step 2: Execute scheduling
    timeline = []

    rr_result, end1 = round_robin(q1, time_quantum=4)
    timeline += rr_result

    fcfs_result, end2 = fcfs(q2, start_time=end1)
    timeline += fcfs_result

    sjf_result, _ = sjf(q3, start_time=end2)
    timeline += sjf_result

    # Step 3: Visualize
    draw_gantt_chart(timeline)
