import string
import random
from . import characters

def generatestring(length:int,upper:bool=True,lower:bool=True,numbers:bool=True,symbols:str=""):
    '''arguments: 
    length: int (Length of the generated string)
    upper:bool (Whether or not to use uppercase chars in the generated string)
    lower:bool (Whether or not to use lowercase chars in the generated string)
    numbers:bool (Whether or not to use numbers in the generated string)
    symbols:string (A list of symbols to use in the generated string)'''
    if upper is False and lower is False:
        return '"upper" and "lower" cant both be False'
    symbolss = symbols
    if len(symbols) > 0:
        symbols = True
    else:
        symbols = False
    if numbers is True and symbols is True:
        generatedstring = "".join(random.choice(characters.ascii_letters + characters.digits + symbolss) for _ in range(length))
    elif numbers is True and symbols is False:
        generatedstring = "".join(random.choice(characters.ascii_letters + characters.digits) for _ in range(length))
    elif numbers is False and symbols is True:
        generatedstring = "".join(random.choice(characters.ascii_letters + symbolss) for _ in range(length))
    else:
        generatedstring = "".join(random.choice(characters.ascii_letters) for _ in range(length))
    if upper is True and lower is True:
        return generatedstring
    elif upper is True and lower is False:
        return generatedstring.upper()
    elif upper is False and lower is True:
        return generatedstring.lower()
