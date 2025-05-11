import random

def generate_number(at: int = -10, to: int = 10) -> float:
    return random.uniform(at, to)

def generate_password(password_length: int) -> str:
    password = ""
    for i in range(password_length):
        password += random.choice(
            [chr(i) for i in range(ord('a'), ord('z'))] +
            [chr(i) for i in range(ord('A'), ord('B'))] +
            [chr(i) for i in range(ord('0'), ord('9'))] + ['@', '!', '_']
        )
    return password

if __name__ == "__main__":
#    print(count_vowels("hello"))