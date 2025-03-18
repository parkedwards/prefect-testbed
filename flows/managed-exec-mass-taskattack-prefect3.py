from prefect import flow, task
from prefect.futures import wait
import requests
import time
import random

@task(log_prints=True)
def connect_n_sleep(n):
  print(f"Connecting... {n}")
  time.sleep(random.uniform(10, 22))
  response = requests.get("https://curlmyip.org/")
  print("MY IP:")
  print(response.text)
j
@flow(log_prints=True)
def mass_task_attack_prefect3():
  futures = []
  for i in range(1000):
    futures.append(connect_n_sleep.submit(i))
  wait(futures)

if __name__ == "__main__":
  mass_task_attack_prefect3()
