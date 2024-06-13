NBA = dict(
    OklahomaCity="Thunder",
    Dallas="Mavericks",
    Boston="Celtics",
    NewYork="Knicks",
    Denver="Nuggets",
)

print(NBA['Toronto'] if 'Toronto' in NBA else False)


def compare_numbers(a, b):
    return "a is greater" if a > b else "b is greater" if b > a else "a and b are equal"

# Example usage:
print(compare_numbers(3, 5))  # Output: b is greater
print(compare_numbers(10, 2))  # Output: a is greater
print(compare_numbers(4, 4))  # Output: a and b are equal


def guess_secret_word(secret_word, max_attempt=5):
    while max_attempt > 0:
        user_input = input("Enter the secret word: ")
        max_attempt -= 1
        print(max_attempt)
        if secret_word == user_input:
            break

# Example usage:
guess_secret_word("python", max_attempt=5)