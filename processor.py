import json

class RobloxProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        try:
            self.validate_data()
            processed = self._transform_data()
            return processed
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return None
        except TypeError as te:
            print(f"TypeError: {te}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def validate_data(self):
        if not isinstance(self.data, dict):
            raise ValueError("Data should be a dictionary")

    def _transform_data(self):
        # Simulate data transformation
        transformed_data = {k: v * 2 for k, v in self.data.items() if isinstance(v, (int, float))}
        return json.dumps(transformed_data)

# Example usage
if __name__ == '__main__':
    data = {'a': 1, 'b': 2, 'c': 'invalid'}
    processor = RobloxProcessor(data)
    result = processor.process_data()
    print("Processed Data:", result)