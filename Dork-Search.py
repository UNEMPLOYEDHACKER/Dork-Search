#!/usr/bin/env/python3
# 
# ===== #
# Tool made in 2024.
# ===== #

########################################################################

# A notice For everone ..
# If you copying anyone's work then give them credit properly 
# Respect everyones work...

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
    print ("\n[x]  This tool is not working on python 2.0 so please Use Python 3.x \n")
    print ("\n\n\t Unemp-Dorks \033[0m😃\n\n")
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
                Author:  Unemployed Hacker
                github:  github.com/UNEMPLOYEDHACKER """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there, are you ready ? 😈 ß\n"
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
    data = input("\n[+] want to Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] hehe everything done successfully, Enjoy \033 \n\n")
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
        dork = input("\n[+] Enter Your Dork : ") 
        number = input("\n[+] How much site you want to Display : ")
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
            print ("\n\n\t\033[1;91m[!] Everything Done Successfully  \033 \n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033 [ Unempl-Dorks \033 ")
    print ("\t\t\033[1;91m[!] Everything Done Successfully  \033 \n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
