import random
import string


def get_secret_keys(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


secret_key = get_secret_keys()
print("Generate a new secret key: ", secret_key)
