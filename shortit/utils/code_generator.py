import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    """A util function that generates the shortcode

    Args:
        size (int, optional): controls how long you want your shortcode to be. Defaults to 6.
        chars ([string], optional): [the main string that will randomize the code generation]. Defaults to string.ascii_lowercase+string.digits.

    Returns:
        [string]: [the generated shortcode that will be saved in the database]
    """
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
    """A better utility function that checks if the shortcode exists first.

    Args:
        instance (ShortUrl): shortUrl instance to be able to access the main Class
        size (int, optional): takes the size and can override the main code generator function. Defaults to 6.

    Returns:
        (string): the new unique short code
    """
    new_code = code_generator(size=size)
    Klass = instance.__class__

    qs_exists = Klass.objects.filter(shortcode=new_code).exists()

    if qs_exists:
        return create_shortcode(size=size)
    return new_code
