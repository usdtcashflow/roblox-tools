import json
import os

DEFAULT_CONFIG = {
    'username': 'player',
    'game_id': 123456,
    'timeout': 30,
    'debug': False
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    user_config = json.load(file)
                    return {**DEFAULT_CONFIG, **user_config}
                except json.JSONDecodeError:
                    print('Error: Invalid JSON format in config file.')
                    return DEFAULT_CONFIG
        else:
            print('Warning: Config file not found. Using default configuration.')
            return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)