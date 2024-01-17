#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #

# ===== #

########################################################################

#REQUEST FOR ALL USER 
# If you copying anyone's then please give them proper credit ..!
# Respect all developers..

#HAPPY HACKING 


########################################################################


from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# Dorks Eye v1.0


if sys.version[0] in "2":
    print ("\n[x] ..HEHE.. Dorks Search Is Not Working On Python 2.0 Use Python 3.0 \n")
    print ("\n\n\tDork Search \033[1;91mI HAPPY HACKING  \033[0m😈\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""
_   _ _   _ _____ __  __ ____    ____   ___  ____  _  ______
| | | | \ | | ____|  \/  |  _ \  |  _ \ / _ \|  _ \| |/ / ___|
| | | |  \| |  _| | |\/| | |_) | | | | | | | | |_) | ' /\___ \

| |_| | |\  | |___| |  | |  __/  | |_| | |_| |  _ <| . \ ___) |
\____/|_| \_|_____|_|  |_|_|     |____/ \___/|_| \_\_|\_\____/

v1.0 """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  UNEMPLOYED HACKER
                Github:  https://github.com/UNEMPLOYEDHACKER\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tARE YOU READY TO DO SOMTHING CRAZY? 😈\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] WANT TO SAVE DORK FILE ? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] EVERYTHING WILL BE DONE SUCCESSFULLY,NOW ENJOY  \033[0m😈\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Enter Your Dork: ")
        amount = input("[+] How Much Dorks You Want To Generate: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] EVERYTHING WILL BE DONE SUCCESSFULLY,NOW ENJOY  \033[0m😈\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mDork Search\033[0m")
    print ("\t\t\033[1;91m[!] EVERYTHING WILL BE DONE SUCCESSFULLY,NOW ENJOY \033[0m😈\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
