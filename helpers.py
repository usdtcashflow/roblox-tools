from typing import List, Dict, Any

def convert_to_dict(list_of_tuples: List[tuple]) -> List[Dict[str, Any]]:
    """
    Convert a list of tuples into a list of dictionaries.

    Args:
        list_of_tuples (List[tuple]): A list where each tuple contains key-value pairs.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries translated from the tuple pairs.
    """
    return [{str(tup[0]): tup[1] for tup in list_of_tuples}]


def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A list of numeric values.

    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def is_user_admin(user_roles: List[str]) -> bool:
    """
    Check if a user has admin rights based on their roles.

    Args:
        user_roles (List[str]): A list of roles assigned to the user.

    Returns:
        bool: True if the user has admin rights, False otherwise.
    """
    return 'admin' in user_roles


def format_username(username: str) -> str:
    """
    Format a username by stripping and lowering it.

    Args:
        username (str): The username to format.

    Returns:
        str: The formatted username.
    """
    return username.strip().lower()