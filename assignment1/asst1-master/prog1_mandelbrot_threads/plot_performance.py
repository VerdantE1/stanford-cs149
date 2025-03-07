import matplotlib.pyplot as plt

# 读取日志文件
threads = []
serial_times = []
thread_times = []
speedups = []

with open("performance_log.txt", "r") as f:
    for line in f:
        data = line.split()
        threads.append(int(data[0]))
        serial_times.append(float(data[1]))
        thread_times.append(float(data[2]))
        speedups.append(float(data[3]))

# 绘制运行时间图
plt.figure(figsize=(10, 5))
plt.plot(threads, serial_times, label="Serial Time (ms)", marker="o")
plt.plot(threads, thread_times, label="Thread Time (ms)", marker="o")
plt.xlabel("Number of Threads")
plt.ylabel("Time (ms)")
plt.title("Serial vs Threaded Mandelbrot Performance")
plt.legend()
plt.grid()
plt.savefig("time_plot.png")  # 保存运行时间图

# 绘制加速比图
plt.figure(figsize=(10, 5))
plt.plot(threads, speedups, label="Speedup", marker="o", color="green")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Threads")
plt.legend()
plt.grid()
plt.savefig("speedup_plot.png")  # 保存加速比图

plt.show()