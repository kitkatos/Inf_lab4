import time


start_time = time.perf_counter()
for i in range(100):
    import main_task
end_time = time.perf_counter()

print(f"Основа - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import dop1_lib
end_time = time.perf_counter()

print(f"Доп 1  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import dop2_reg
end_time = time.perf_counter()

print(f"Доп 2  - {end_time - start_time}")
