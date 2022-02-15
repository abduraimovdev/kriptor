
import hashlib
import os
import datetime
from termcolor import colored

x = datetime.datetime.now()
x = x.strftime("%c")
logo = colored("""
    +------------------------------------------+
    |              Dehash Dastur
    |
    |   Author & GitHub: AbduraimovDev
    |                                          
    |   {}
    |
    |___[1] MD5 DEHASH
    |                             
    |___[2] SHA1 DEHASH
    |
    |___[3] SHA224 DEHASH
    |
    |___[4] SHA256 DEHASH
    |
    |___[5] SHA512 DEHASH
    |
    +------------------------------------------+
""", 'green').format(x)

os.system("clear")
print("\n" + logo)
ans = input(colored("\n[*] Iltimos Raqam Tanlang [*]:", 'yellow', attrs=['bold']))

## MD5
def md5_f():
    md5_hash = input(colored("[*]-- MD5 CODE --[*]:", 'green', attrs=['bold', 'blink']))
    password_list = open("password.txt", 'r')

    for password in password_list.readlines():
        password = password.strip("\n")
        hash_t = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        if hash_t == md5_hash:
            print(colored("--#--SHA224 CODE OCHILDI--#-[" + password + "]--#--", 'green', attrs=['bold']))
            quit()
        else:
            print(colored("[*]--" + hash_t + "--[*]", 'red', attrs=['bold']))        
    
    print(colored("xxx-[-HASH OCHILMADI-]-xxx", 'yellow', attrs=['bold', 'blink']))

## SHA1
def sha1_f():
    sha1_hash = input(colored("[*]-- SHA1 CODE --[*]:", 'green', attrs=['bold', 'blink']))
    password_list = open("password.txt", 'r')

    for password in password_list.readlines():
        password = password.strip("\n")
        hash_t = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
        if hash_t == sha1_hash:
            print(colored("--#--SHA224 CODE OCHILDI--#-[" + password + "]--#--", 'green', attrs=['bold']))
            quit()
        else:
            print(colored("[*]--" + hash_t + "--[*]", 'red', attrs=['bold']))        
    
    print(colored("xxx-[-HASH OCHILMADI-]-xxx", 'yellow', attrs=['bold', 'blink']))

## SHA224
def sha224_f():
    sha224_hash = input(colored("[*]-- SHA224 CODE --[*]:", 'green', attrs=['bold', 'blink']))
    password_list = open("password.txt", 'r')

    for password in password_list.readlines():
        password = password.strip("\n")
        hash_t = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
        if hash_t == sha224_hash:
            print(colored("--#--SHA224 CODE OCHILDI--#-[" + password + "]--#--", 'green', attrs=['bold']))
            quit()
        else:
            print(colored("[*]--" + hash_t + "--[*]", 'red', attrs=['bold']))        
    
    print(colored("xxx-[-HASH OCHILMADI-]-xxx", 'yellow', attrs=['bold', 'blink']))

## SHA256
def sha256_f():
    sha256_hash = input(colored("[*]-- SHA256 CODE --[*]:", 'green', attrs=['bold', 'blink']))
    password_list = open("password.txt", 'r')

    for password in password_list.readlines():
        password = password.strip("\n")
        hash_t = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        if hash_t == sha256_hash:
            print(colored("--#--SHA224 CODE OCHILDI--#-[" + password + "]--#--", 'green', attrs=['bold']))
            quit()
        else:
            print(colored("[*]--" + hash_t + "--[*]", 'red', attrs=['bold']))        
    
    print(colored("xxx-[-HASH OCHILMADI-]-xxx", 'yellow', attrs=['bold', 'blink']))

## SHA512
def sha512_f():
    sha512_hash = input(colored("[*]-- SHA512 CODE --[*]:", 'green', attrs=['bold', 'blink']))
    password_list = open("password.txt", 'r')

    for password in password_list.readlines():
        password = password.strip("\n")
        hash_t = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
        if hash_t == sha512_hash:
            print(colored("--#--SHA224 CODE OCHILDI--#-[" + password + "]--#--", 'green', attrs=['bold']))
            quit()
        else:
            print(colored("[*]--" + hash_t + "--[*]", 'red', attrs=['bold']))        
    
    print(colored("xxx-[-HASH OCHILMADI-]-xxx", 'yellow', attrs=['bold', 'blink']))


if ans == "1":
    md5_f()
elif ans == "2":
    sha1_f()
elif ans == "3":
    sha224_f()
elif ans == "4":
    sha256_f()
elif ans == "5":
    sha512_f()
else:
    print(colored("XATO", 'red', attrs=['bold', 'blink']))    
    


