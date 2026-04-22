import json
import os

class ConfigLoader:
    def __init__(self, config_file='config.json', defaults=None):
        self.config_file = config_file
        self.defaults = defaults if defaults else {}
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            return self.defaults
        with open(self.config_file, 'r') as file:
            try:
                user_config = json.load(file)
            except json.JSONDecodeError:
                print('Error reading the JSON configuration file.')
                return self.defaults
            return {**self.defaults, **user_config}

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    defaults = {
        'host': 'localhost',
        'port': 8080
    }
    config_loader = ConfigLoader(defaults=defaults)
    print(config_loader.get('host'))  # Outputs the host from the config or defaults
