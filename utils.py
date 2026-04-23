import time
import requests
from functools import wraps


def retry(max_attempts=3, delay=1):
    """Decorator to retry a function upon exceptions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.ConnectionError, 
                        requests.exceptions.Timeout) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=5, delay=2)
def fetch_data(url):
    """Fetch data from a given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except Exception as e:
        print(f'Failed to fetch data: {e}')