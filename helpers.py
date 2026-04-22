from typing import List, Dict


def calculate_average(scores: List[int]) -> float:
    """
    Calculate the average of a list of scores.

    Parameters:
        scores (List[int]): A list of integer scores.

    Returns:
        float: The average of the scores, or 0.0 if the list is empty.
    """    
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def format_scoreboard(scores: Dict[str, int]) -> str:
    """
    Format a scoreboard from a dictionary of player scores.

    Parameters:
        scores (Dict[str, int]): A dictionary where keys are player names and values are scores.

    Returns:
        str: A formatted string displaying the scores of all players.
    """    
    formatted_scores = [f'{player}: {score}' for player, score in scores.items()]
    return '\n'.join(formatted_scores)


def is_valid_score(score: int) -> bool:
    """
    Check if the given score is valid (between 0 and 100).

    Parameters:
        score (int): The score to validate.

    Returns:
        bool: True if the score is valid, False otherwise.
    """    
    return 0 <= score <= 100

