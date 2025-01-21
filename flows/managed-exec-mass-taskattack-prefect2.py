from prefect import flow, task
import time

@task(log_prints=True)
def connect_n_sleep(n):
  print(f"Connecting... {n}")
  time.sleep(30)

@flow(log_prints=True)
def mass_task_attack_prefect2():
  futures = []
  for i in range(1000):
    futures.append(connect_n_sleep.submit(i))

if __name__ == "__main__":
  mass_task_attack_prefect2()
