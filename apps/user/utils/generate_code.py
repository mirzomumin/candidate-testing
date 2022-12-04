from random import randint

def generate_code():
    '''Generate email confirmation code'''
    code = randint(100_000, 999_999)
    return code