from string import ascii_lowercase
from typing import Tuple
import secrets # Uses TRNG - True Random Number Generator


def generate_portion( portion_size:int ) -> str:
    """
    Generates a random string of lowercase letters.

    Args:
        portion_size: The desired length of the generated string.

    Returns:
        A string of random lowercase letters with a length equal to `portion_size`.
    """
    portion = ""
    for _ in range( portion_size ):
        portion += secrets.choice( ascii_lowercase )
    
    return portion


def generate_meeting_id( pattern: Tuple[int, int, int] ):
    """
    Generates a unique meeting ID based on a specified pattern.

    This function creates a meeting ID string consisting of three random portions of
    lowercase letters, separated by hyphens. The length of each portion is
    determined by the integers in the input tuple.

    Args:
        pattern: A tuple of three integers (e.g., `(4, 3, 5)`), where each integer
            specifies the length of a corresponding portion in the meeting ID.

    Returns:
        A string representing the formatted meeting ID, such as "abcd-efg-hijkl".
    """
    a, b, c = pattern

    pattern = ""
    pattern += generate_portion( a ) + "-"
    pattern += generate_portion( b ) + "-"
    pattern += generate_portion( c )

    return pattern


if __name__ == "__main__":
    print( generate_meeting_id( (4, 3, 4) ) )