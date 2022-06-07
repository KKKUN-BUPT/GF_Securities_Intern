import psutil
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))


print(psutil.virtual_memory())

psutil.test()