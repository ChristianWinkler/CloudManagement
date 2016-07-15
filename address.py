"""Helper functions to generate random input data."""

import random
import string

def generateName(minLenght=1, maxLength=255):
    """Generated a random password of the given length."""
    chars = string.ascii_letters + string.digits
    size = random.randint(minLenght, maxLength)
    return ''.join(random.choice(chars) for _ in range(size))
    NewName = generateName(5, 30)   

def generateAddress(minLenght=1, maxLength=255):
    """Generated a random password of the given length."""
    chars = string.ascii_letters + ' , ' + string.digits
    size = random.randint(minLenght, maxLength)
    return ''.join(random.choice(chars) for _ in range(size))
    NewAddress = generateAddress(6, 50)

def generateCity(minLenght=1, maxLength=255):
    """Generated a random password of the given length."""
    chars = string.ascii_letters
    size = random.randint(minLenght, maxLength)
    return ''.join(random.choice(chars) for _ in range(size))
    NewCity = generateCity(3, 20)

def generatePostcode(minLenght=1, maxLength=8):
    """Generated a random password of the given length."""
    chars = string.digits
    size = random.randint(minLenght, maxLength)
    return ''.join(random.choice(chars) for _ in range(size))
    NewPostcode = generatePostcode(2, 8)