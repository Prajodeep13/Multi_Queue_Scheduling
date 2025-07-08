import matplotlib.pyplot as plt

def draw_gantt_chart(timeline):
    fig, gnt = plt.subplots()
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Processes")
    gnt.set_yticks([i * 10 for i in range(len(timeline))])
    gnt.set_yticklabels([task[0] for task in timeline])
    gnt.grid(True)

    for i, (pid, start, end) in enumerate(timeline):
        gnt.broken_barh([(start, end - start)], (i * 10 - 4, 8), facecolors=('tab:blue'))

    plt.title("Gantt Chart: Multi-Level Queue Scheduling")
    plt.show()
