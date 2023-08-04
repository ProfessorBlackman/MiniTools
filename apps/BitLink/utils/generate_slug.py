import secrets
import string


def generate_slug() -> string:
    characters = string.ascii_lowercase + string.digits
    result_str = ''.join(secrets.choice(characters) for _ in range(6))  # generate slug from ascii
    return result_str
