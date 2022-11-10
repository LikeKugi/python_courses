def get_reply(number: int) -> str | int:
    """Fizz Buzz"""
    return ('Fizz' * (not number % 3) + 'Buzz' * (not number % 5)) or number


def main():
    for i in range(20):
        print(get_reply(i))

if __name__ == '__main__':
    main()