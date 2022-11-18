import re
import hashlib
import getpass
import pyperclip


# config
HASH_SORTS = 2 ** 18
SALT = 'o60sme9GtQB9fiPVt59DeOrPXPEG41dBMVkTbcg'
BITS_TO_INT_LEN = 20
PASSWORD_LEN = 16
PASSWORD_CHARS = [
    'abcdefghijklmnopqrstuvwxyz',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '1234567890',
    '!@#$%^&*()',
]

def checkPasswordValid(password):
    lowercase = bool(re.search('[a-z]', password))
    uppercase = bool(re.search('[A-Z]', password))
    number = bool(re.search('[0-9]', password))
    symbol = bool(re.search('[!@#$%^&*\(\)]', password))
    return lowercase and uppercase and number and symbol


if __name__ == '__main__':
    domain = input('Website domain: ')
    password = getpass.getpass('Master password: ')
    print('Generating a password...')
    h = 0

    s = domain + '/' + password
    for i in range(HASH_SORTS):
        h = hashlib.sha256(s.encode())
        s = h.digest().hex()
        s += ''.join(sorted(s))

    tail = 0
    p = ''
    while not checkPasswordValid(p):
        s2 = s + '/' + str(tail)
        p = ''
        for j in range(PASSWORD_LEN):
            h = hashlib.sha256((s2 + '/' + str(j)).encode())
            k = int.from_bytes(h.digest()[:BITS_TO_INT_LEN], "little")
            chars = PASSWORD_CHARS[k % len(PASSWORD_CHARS)]
            p += chars[k % len(chars)]
        tail += 1
    
    pyperclip.copy(p)
    print(f'Password copied to clipboard!')

