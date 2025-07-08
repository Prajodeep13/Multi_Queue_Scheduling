def round_robin(queue, time_quantum):
    time = 0
    timeline = []

    while queue:
        process = queue.pop(0)
        if process.start_time == -1:
            process.start_time = time

        exec_time = min(time_quantum, process.remaining_time)
        time += exec_time
        process.remaining_time -= exec_time

        timeline.append((process.pid, time - exec_time, time))

        if process.remaining_time > 0:
            queue.append(process)
        else:
            process.completion_time = time

    return timeline, time
