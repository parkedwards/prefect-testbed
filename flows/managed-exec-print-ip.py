from prefect import flow
import requests

@flow(log_prints=True)
def print_my_ip():
  response = requests.get("https://curlmyip.org/")
  print("MY IP:")
  print(response.text)