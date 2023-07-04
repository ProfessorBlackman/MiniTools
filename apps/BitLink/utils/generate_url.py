import secrets
import string

from decouple import config


#  function to generate short url from long url
def urlgen(long):
    """
        Generates a short url

        Uses secrets library, and defines a pool of characters using the strings library.
        Then creates a new url it the generated string.

        Parameters:
        ----------
        long : str(url)
            A url to be shortened

        Returns:
        -------
        tuple
            returns a tuple of (new_url, result_str).
        """
    characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(secrets.choice(characters) for _ in range(6))  # generate slug from ascii
    # characters
    new_url = f'{config("DOMAIN")}{result_str}'
    print("Random string of length", long, "is:", result_str)
    print(new_url)

    return new_url, result_str
