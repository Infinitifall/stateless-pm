import re
import hashlib
import getpass

import pyperclip


def checkOneOfEach(password : str, chars_list: list):
    for each_chars in chars_list:
        if not bool(re.search('[' + re.escape(each_chars) + ']', password)):
            return False
    return True


def generatePassword(domain: str, password: str, chars_list: list):
    salt = 'o60sme9GtQB9fiPVt59DeOrPXPEG41dBMVkTbcg'
    hash_sorts = 2 ** 18
    hex_to_int_len = 4
    separator = "/"
    password_len_max = 10000

    # generate s by repeated hashing and sorting
    # this should make brute forcing the master password prohibitively expensive
    h = 0
    s = domain + separator + password
    for i in range(hash_sorts):
        h = hashlib.sha256(s.encode())
        s = h.hexdigest()
        s += ''.join(sorted(s)) + salt

    # generate passwords, appending tail
    # and repeat until password is valid
    tail = 0
    p = ''
    while not checkOneOfEach(p, chars_list):
        s2 = s + separator + str(tail)
        p = ''
        for j in range(password_len_max):
            h = hashlib.sha256((s2 + separator + str(j)).encode())
            k1 = int(h.hexdigest()[:hex_to_int_len], 16)
            k2 = int(h.hexdigest()[:-hex_to_int_len-1], 16)
            chars = chars_list[k1 % len(chars_list)]
            p += chars[k2 % len(chars)]
    return p


def getInputYesNo(message_string: str, default_option: bool):
    option_string = '[Y/n]' if default_option else '[y/N]'
    ask_string = ''
    while not (ask_string.lower() == 'n' or ask_string.lower() == 'y'):
        ask_string = input(f'{message_string} {option_string} ')
        if len(ask_string) == 0:
            return default_option
    return True if ask_string.lower() == 'y' else False


def getInputInt(message_string: str, default_option: int):
    # choose password length
    int_string = ''
    while True:
        int_string = input(f'{message_string} (default {default_option}): ')
        if len(int_string) == 0:
            return default_option
        try:
            int_string = int(int_string)
            return int_string
        except Exception as e:
            pass


def passwordPrompt():
    tail_salt = 'P79X5s3JVDXc779B9qki5D1qLF5RwogPDN51NqR'
    password_len = 16
    password_chars = {
        'lowercase': {
            'allowed': True,
            'chars': 'abcdefghijklmnopqrstuvwxyz'
        },
        'uppercase': {
            'allowed': True,
            'chars': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        },
        'numbers': {
            'allowed': True,
            'chars': '1234567890'
        },
        'special': {
            'allowed': True,
            'chars': '!@#$%^&*()'
        }
    }

    print('')
    
    # get website domain
    website_domain = ''
    while not len(website_domain) > 0:
        website_domain = input('Enter Website domain or App name: ')
    if website_domain[-1] == '/':
        website_domain = website_domain[0:-1]
    
    # get master password
    master_password = ''
    while not len(master_password) > 0:
        master_password = getpass.getpass('Master password (invisible): ')
    
    # get whether to use default settings
    default_settings = getInputYesNo('Use default settings?', True)
    if not default_settings:
        # choose password length
        password_len = getInputInt('Enter password length', password_len)
        
        # choose allowed password chars
        for my_key in password_chars:
            allowed = getInputYesNo(f'Include "{my_key}" characters?', True)
            if not allowed:
                password_chars[my_key]['allowed'] = False
    
    # generate the passwords
    i = 0
    another_password = True
    while another_password:
        # generate chars_list from password_chars dict
        chars_list = []
        for my_key in password_chars:
            chars_list.append(password_chars[my_key]['chars'])
        
        # generate the password
        print('Generating a password...')
        password_gen = generatePassword(website_domain + i * tail_salt, master_password, chars_list)
        password_final = ''
        j = 0
        while len(password_final) < password_len and j < len(password_gen):
            curr_char = password_gen[j]
            for my_key in password_chars:
                if curr_char in password_chars[my_key]['chars']:
                    if password_chars[my_key]['allowed']:
                        password_final += curr_char
                    else:
                        pass
            j += 1
        
        # check if password generation failed
        if len(password_final) < password_len:
            print('Couldn\'t generate password :(')
            print('Either password length requested is too long or you are one in a Quintillion :)')
            return -1
        
        # give user the generated password
        try:
            pyperclip.copy(password_final)
            print(f'Password copied to clipboard!')
        except Exception as e:
            print('Couldn\'t copy password to clipboard')
            terminal_print = getInputYesNo('Print password to terminal instead?', True)
            if terminal_print:
                print(f'\nPassword {i}:\n\t\t {password_final}\n')
        
        i += 1
        another_password = getInputYesNo('Generate alternative password?', False)
    
    print('')
    return 0


if __name__ == '__main__':
    passwordPrompt()