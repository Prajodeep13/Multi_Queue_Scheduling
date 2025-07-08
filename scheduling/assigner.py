def assign_to_queues(processes):
    q1, q2, q3 = [], [], []

    for process in processes:
        if process.priority == 1:
            q1.append(process)
        elif process.priority == 2:
            q2.append(process)
        else:
            q3.append(process)

    return q1, q2, q3
