import matplotlib.pyplot as plt

def parse_log(file_path):
    conversion_times = []
    cpu_usages = []
    memory_usages = []

    with open(file_path, 'r') as file:
        for line in file:
            if "Conversion time:" in line:
                conversion_time = float(line.split("Conversion time: ")[1].strip().split()[0])
                conversion_times.append(conversion_time)
            elif "CPU Usage:" in line:
                cpu_usage = float(line.split("CPU Usage: ")[1].strip().split()[0].replace('%', ''))
                cpu_usages.append(cpu_usage)
            elif "Memory Usage:" in line:
                memory_usage = float(line.split("Memory Usage: ")[1].strip().split()[0].replace('%', ''))
                memory_usages.append(memory_usage)

    return conversion_times, cpu_usages, memory_usages

def plot_metrics(conversion_times, cpu_usages, memory_usages):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.plot(conversion_times, label='Conversion Time (s)')
    plt.xlabel('Requests')
    plt.ylabel('Time (s)')
    plt.title('Conversion Time')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(cpu_usages, label='CPU Usage (%)', color='orange')
    plt.xlabel('Requests')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.plot(memory_usages, label='Memory Usage (%)', color='green')
    plt.xlabel('Requests')
    plt.ylabel('Memory Usage (%)')
    plt.title('Memory Usage')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_file_path = 'C:/Users/srini/Downloads/trisha_cloud/performance.log'  # Update with the correct path
    conversion_times, cpu_usages, memory_usages = parse_log(log_file_path)
    plot_metrics(conversion_times, cpu_usages, memory_usages)

