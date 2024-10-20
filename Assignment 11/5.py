import time
current_time = time.strftime("%H:%M:%S", time.localtime())
print(f"Current time: {current_time}")
time.sleep(3)
new_time = time.strftime("%H:%M:%S", time.localtime())
print(f"Time after 3 seconds: {new_time}")