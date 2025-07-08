def fcfs(queue, start_time):
    time = start_time
    timeline = []

    for process in sorted(queue, key=lambda p: p.arrival_time):
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        time += process.burst_time
        process.completion_time = time
        timeline.append((process.pid, process.start_time, time))

    return timeline, time
