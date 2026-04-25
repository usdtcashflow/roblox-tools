from typing import Any, Dict

class RobloxUser:
    """
    A class representing a user in Roblox.
    """
    def __init__(self, username: str, user_id: int) -> None:
        """
        Initializes the RobloxUser with a username and user ID.
        :param username: The username of the Roblox user.
        :param user_id: The unique ID of the Roblox user.
        """
        self.username: str = username
        self.user_id: int = user_id

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the RobloxUser instance to a dictionary.
        :return: A dictionary representation of the RobloxUser instance.
        """
        return {
            'username': self.username,
            'user_id': self.user_id
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'RobloxUser':
        """
        Creates a RobloxUser instance from a dictionary.
        :param data: A dictionary containing user information.
        :return: An instance of RobloxUser.
        """
        return RobloxUser(data['username'], data['user_id'])

# Example Usage
if __name__ == '__main__':
    user_data = {'username': 'Player1', 'user_id': 123456}
    user = RobloxUser.from_dict(user_data)
    print(user.to_dict())
