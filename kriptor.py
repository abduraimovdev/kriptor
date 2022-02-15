
import hashlib
import os
import datetime
from termcolor import colored

x = datetime.datetime.now()
x = x.strftime("%c")
logo = colored("""
    +------------------------------------------+
    |             Kriptor Dastur
    |
    |   Author & GitHub: AbduraimovDev
    |
    |   {}
    |
    |___[1] HASH
    |
    |___[2] DEHASH
    |
    +------------------------------------------+
""", 'green').format(x)

os.system("clear")
print("\n" + logo)
ans = input(colored("\n[*] Iltimos Raqam Tanlang [*]:", 'yellow', attrs=['bold']))

if ans == "1":
    os.system("python3 hash.py")
elif ans == "2":
    os.system("python3 dehash.py")
