# Stateless Password Manager

A password manager without any storage (stateless). Passwords are generated from scratch each time, given a Website domain / App name and a master password. The process is deterministic and will produce the same password at any time and on any device.

- Smaller attack surface - there is nothing to hack
- No password syncing - there is nothing to sync


## Install

- **Windows**
    1. Have [Python](https://www.python.org/downloads/) installed
    2. [Download stateless-pm](https://github.com/Infinitifall/stateless-pm/archive/refs/heads/main.zip) and unzip the folder
    3. Double click on `run_on_windows.bat`


- **Linux/macOS/BSD**
    ```bash
    # clone repo
    git clone https://github.com/Infinitifall/stateless-pm
    cd stateless-pm
    
    # run
    ./run_on_linux.sh
    ```


## Run

- Generating a password for a website
    ```
    $ ./run_on_linux.sh

    Enter Website domain or App name: wikipedia.org
    Master password (invisible):
    Use default settings? [Y/n]
    Generating a password...
    Couldn't copy password to clipboard
    Print password to terminal instead? [Y/n]

    Password 0:
                    )MZ9(O2N%P9$IU38

    Generate alternative password? [y/N] n

    ```

- Generating a 6 digit pin

    ```
    $ ./run_on_linux.sh

    Enter Website domain or App name: examplebank.com
    Master password (invisible):
    Use default settings? [Y/n] n
    Enter password length (default 16): 6
    Include "lowercase" characters? [Y/n] n
    Include "uppercase" characters? [Y/n] n
    Include "numbers" characters? [Y/n]
    Include "special" characters? [Y/n] n
    Generating a password...
    Couldn't copy password to clipboard
    Print password to terminal instead? [Y/n]

    Password 0:
                    662188

    Generate alternative password? [y/N] n

    ```

- Generating multiple passwords for multiple accounts

    ```
    $ ./run_on_linux.sh

    Enter Website domain or App name: Instagram
    Master password (invisible):
    Use default settings? [Y/n]
    Generating a password...
    Couldn't copy password to clipboard
    Print password to terminal instead? [Y/n]

    Password 0:
                    (!jh!&e0I6VjDY2q

    Generate alternative password? [y/N] y
    Generating a password...
    Couldn't copy password to clipboard
    Print password to terminal instead? [Y/n]

    Password 1:
                    !z*s9@s(ukoD7We8

    Generate alternative password? [y/N] y
    Generating a password...
    Couldn't copy password to clipboard
    Print password to terminal instead? [Y/n]

    Password 2:
                    &o2a71@^09ut5I(Y

    Generate alternative password? [y/N] n

    ```

