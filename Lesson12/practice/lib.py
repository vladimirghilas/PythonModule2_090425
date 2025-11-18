import random


def generate_number(at: int = -10, to: int = 10) -> float:
    return random.uniform(at, to)


def generate_password(password_length: int = 12) -> str:
    characters = (
            [chr(i) for i in range(ord('a'), ord('z') + 1)] +
            [chr(i) for i in range(ord('A'), ord('Z') + 1)] +
            [chr(i) for i in range(ord('0'), ord('9') + 1)] +
            ['@', '!', '_']
    )
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password


if __name__ == "__main__":
    print(generate_password())
