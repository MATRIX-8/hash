from hashlib import *
import time
import os


def error():
    print(' /n \033[1;91m [!] Error The Number [!] ')


def ab():
    md5(Nume.encode()).hexdigest()
    print('[√] lodinge Whait ...')
    time.sleep(4)
    print("[√] Hash is >>", md5)


def cd():
    sha224(Nume.encode()).hexdigest()
    print('[√] lodinge Whait ...')
    time.sleep(4)
    print("[√] Hash is >>", sha224)


def ef():
    sha384(Nume.encode()).hexdigest()
    print('[√] lodinge Whait ...')
    time.sleep(4)
    print("[√] Hash is >>", sha384)


def jh():
    sha512(Nume.encode()).hexdigest()
    print('[√] lodinge Whait ...')
    time.sleep(4)
    print("[√] Hash is >>", sha512)


# ========== LOGO==========#

logo = ('''\033[1;91m

	                       $BY: badrddin mermouchi √
            +=======================================+
            |..........cryptography v 2    .........|
            +---------------------------------------+
            |#By: Bdrddin Mer                       |
            |#Fb: www.fb.com/matrix69               |
            |#Date: 02/03/2021                      |
            |                           ^_^ !!!     |
            +=======================================+
            |..........cryptography v 2    .........|
            +---------------------------------------+

    ''')
badr = ('''             Welcome, to the world of #CRYPTOGRAPHY

''')

a = ('[01] $> md5')
b = ('[02] $> sha224')
c = ('[03] $> sha384')
d = ('[04] $> sha512')
print(logo)
time.sleep(1)
print('\033[0;32m', badr)
time.sleep(0.5)
print('\033[0;32m', a)
print('\033[0;32m', b)
print('\033[0;32m', c)
print('\033[0;32m', d)
print("")
number = int(input('[+] Tybe The Number  :'))
if number == 1:
    try:
        time.sleep(1)
        Nume = input('[+] Type in text that you want to encrypt :')
        time.sleep(2)
        ab()


    except ValueError:

        error()


if number == 2:
    try:
        time.sleep(1)
        Nume = input('[+] Type in text that you want to encrypt :')
        time.sleep(2)
        cd()


    except ValueError:

        error()


if number == 3:
    try:
        time.sleep(1)
        Nume = input('[+] Type in text that you want to encrypt :')
        time.sleep(2)
        ef()

    except ValueError:

        error()


if number == 4:
    try:
        time.sleep(1)
        Nume = input('[+] Type in text that you want to encrypt :')
        time.sleep(2)
        jh()
    except ValueError:

        error()
