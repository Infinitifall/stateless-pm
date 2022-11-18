# Stateless Password Manager

A stateless password manager. No passwords are ever stored locally, instead it generates the same password for a given combination of domain and master password. The domain and master password are combined with a salt and hashed and sorted $2^{18}$ times, making brute forcing passwords prohibitively expensive.

Install dependencies

```
pip install pyperclip
```

Run

```
$ python password.py
Website domain: wikipedia.org
Master password: 
Generating a password...
Password copied to clipboard!
```
