def sjf(queue, start_time):
    time = start_time
    timeline = []

    processes = sorted(queue, key=lambda p: (p.arrival_time, p.burst_time))

    while processes:
        available = [p for p in processes if p.arrival_time <= time]
        if not available:
            time += 1
            continue
        shortest = min(available, key=lambda p: p.burst_time)
        processes.remove(shortest)
        shortest.start_time = time
        time += shortest.burst_time
        shortest.completion_time = time
        timeline.append((shortest.pid, shortest.start_time, time))

    return timeline, time
