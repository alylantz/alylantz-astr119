import requests
import time
url = input("url: ")
url = 'http://ucsc.edu'
response = requests.get(url)
nbytes = len(response.content)

print(f"{nbytes} bytes read from {url}")
start_time = time.perf_counter()
response = requests.get(url)
end_time = time.perf_counter()
nbytes = len(response.content)
elapsed_time = end_time - start_time
nbytes = len(response.content)
elapsed_time = end_time - start_time
megabytes = nbytes / 1_000_000
rate = megabytes / elapsed_time if elapsed_time > 0 else 0
print(f"{nbytes} bytes ({megabytes:.4f} MB) read from {url}")
print(f"Time elapsed: {elapsed_time:.4f} seconds")
print(f"Download rate: {rate:.4f} MB/s")

