import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'password': '',
    'game_id': 0,
    'server_region': 'US',
    'debug_mode': False
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    config_data = json.load(file)
                    return {**DEFAULT_CONFIG, **config_data}
                except json.JSONDecodeError:
                    print('Error decoding JSON, using defaults.')
        return DEFAULT_CONFIG

    def get_config(self):
        return self.config

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get_config())