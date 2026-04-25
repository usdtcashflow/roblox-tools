import time
import requests

class NetworkException(Exception):
    pass

def retry_network_operation(func, max_retries=3, delay=2, *args, **kwargs):
    attempts = 0
    while attempts < max_retries:
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise NetworkException(f'Operation failed after {max_retries} attempts') from e
            time.sleep(delay)

# Example network function that uses retry logic

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP errors
    return response.json()

if __name__ == '__main__':
    try:
        data = retry_network_operation(fetch_data, url='https://api.example.com/data')
        print(data)
    except NetworkException as ne:
        print(str(ne))