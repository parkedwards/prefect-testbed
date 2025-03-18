from prefect import flow
import random
import requests
import asyncio

@flow
async def attacking_subflow(n):
  print(f"Connecting... {n}")
  await asyncio.sleep(random.uniform(3, 7))
  response = requests.get("https://curlmyip.org/")
  print("MY IP:")
  print(response.text)

@flow
async def mass_flow_attack(count: int = 5):
  coros = [attacking_subflow(i) for i in range(count)]
  await asyncio.gather(*coros)

if __name__ == "__main__":
  asyncio.run(mass_flow_attack())

