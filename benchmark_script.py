import time
import psutil

def benchmark():
    print("Benchmarking CPU and memory usage...")
    print("CPU usage (%):", psutil.cpu_percent(interval=1))
    print("Memory usage (%):", psutil.virtual_memory().percent)

if __name__ == "__main__":
    start = time.time()
    benchmark()
    end = time.time()
    print("Latency: %.2f seconds" % (end - start))
