import requests
import concurrent.futures
import time

# Define the API endpoint
# api_url = 'https://api.example.com/your-endpoint'
api_url = 'http://localhost/api/news'
# api_url = 'http://52.194.224.176/api/news'

# Define the number of requests to send
total_requests = 1000
# Define the number of concurrent workers
concurrent_workers = 50


# Function to send a single request
def send_request():
    response = requests.get(api_url)
    return response.status_code


def main():
    # Measure the start time
    start_time = time.time()

    # Use ThreadPoolExecutor to send requests concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_workers) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(send_request) for _ in range(total_requests)]

        # Wait for all futures to complete and collect the results
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    # Measure the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Calculate QPS (Queries Per Second)
    qps = total_requests / elapsed_time

    print(f"Total Requests: {total_requests}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"QPS: {qps:.2f}")

    # Optionally, print the status codes of the responses
    status_code_counts = {}
    for status_code in results:
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

    print("Status Code Counts:")
    for status_code, count in status_code_counts.items():
        print(f"{status_code}: {count}")


if __name__ == '__main__':
    main()
