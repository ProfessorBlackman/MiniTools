import secrets
import string

from decouple import config

from apps.BitLink.utils.generate_slug import generate_slug


#  function to generate short url from long url
def urlgen():
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
    result_str = generate_slug()
    # characters
    new_url = f'{config("DOMAIN")}{result_str}'

    return new_url, result_str
