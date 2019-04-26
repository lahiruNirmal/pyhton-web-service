from random import choice
import string

def generatePwd(length=8, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

# print generatePwd(12, string.letters)