import random
from string import ascii_lowercase
from typing import Tuple
import numpy as np
# import secrets # Uses TRNG - True Random Number Generator

# This is the simplest way to generate a meeting id

def generate_portion( portion_size:int ):
    """
    Generates a random string of lowercase letters.

    Args:
        portion_size: The desired length of the generated string.

    Returns:
        A string of random lowercase letters with a length equal to `portion_size`.
    """
    letters = list( ascii_lowercase ) # Preferred lowercase because of url mappings
    # Convert the letters list to a numpy array
    letters = np.array( letters )

    # Generate random letters with numpy's random.choice method
    random_letters:str = ''.join( np.random.choice( letters, size=portion_size ) )

    return random_letters


def generate_meeting_id( pattern: tuple[int, int, int] ):
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