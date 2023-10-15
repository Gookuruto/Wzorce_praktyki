"""bad practice module."""
from typing import List


def add_numbers(number_1: int, number_2: int, number_3: int) -> None:
    """Add three numbers and print them.

    Description
    """
    result = number_1 + number_2 + number_3
    while True:
        while True:
            while True:
                while True:
                    print(result)
                    break


def edit_users(
    data: List[str],
    nowe_super_dane: List[str],
    super_perfix: str,
    super_extra_prefix: str,
    super_imona: List[str],
) -> List[str]:
    """Add dr. prefix to each user in data."""
    # Read names algorith step.
    user = [name[:10] for name in data]
    # Add prefix to user names.
    users = [f"Dr. {name}" for name in user]
    # Return new users list
    return users


a = [1, 2, 3]
b = [1, 2, 2]

if a is b:
    print("10 to nie 50")

# x(1, 2, 3)

TAU = 256

TAU += 1  # nie zmieniamy stałych nazywanych wielkimi literami
