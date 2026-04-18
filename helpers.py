import random

class RobloxHelper:
    @staticmethod
    def generate_random_id(length=6):
        """Generate a random ID consisting of uppercase letters and digits."""
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def format_username(username):
        """Format the username to a standard format."""
        return username.strip().lower().replace(' ', '_')

    @staticmethod
    def validate_game_id(game_id):
        """Check if the given game ID is a valid int."""
        return isinstance(game_id, int) and game_id > 0

    @staticmethod
    def calculate_playtime(start_time, end_time):
        """Calculate the playtime in minutes."""
        return (end_time - start_time).total_seconds() / 60

    @staticmethod
    def extract_words(text):
        """Extract and return a list of words from the text."""
        return text.split()  
