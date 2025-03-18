from prefect import flow, task
import time
import random
import requests

@task(log_prints=True)
def connect_n_sleep(n):
  print(f"Connecting... {n}")
  time.sleep(random.uniform(10, 22))
  response = requests.get("https://curlmyip.org/")
  print("MY IP:")
  print(response.text)

@flow(log_prints=True)
def mass_task_attack_prefect2():
  futures = []
  for i in range(1000):
    futures.append(connect_n_sleep.submit(i))

if __name__ == "__main__":
  mass_task_attack_prefect2()
