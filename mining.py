import os
import time
from random import randint
import random
import sys

os.system("clear")

listName = []
name = ""
temp = 0
listSeed = ["tor", "an", "rap", "ri", "kal", "cal", "oo",
            "z", "x", "ch", "rea", "ct", "hoo", "sh", "x", "ian",
            "on", "si", "dra", "lla", "ve", "pha", "tiny",
            "tic", "pop", "li", "rela", "ook", "vey",
            "shea", "lib", "lif", "ay", "do", "mi", "si", "let", "bit",
            "in", "ele", "va", "to", "la",
            "st", "rix", "leo", "neo", "ubm",
            "cod", "gic", "bio", "ture", "elec", "now", "nic", "it",
            "it", "too", "eep", "q", "w", "e", "r", "t", "y", "u", "i",
            "v", "c", "x", "z", "l", "k", "j", "h", "g", "f", "d", "s", "a",
            "p", "o", "val", "var", "co", "mi", "lio",
            "b", "n", "m", "un", "us", "cu", "ro", "sha", "ver",
            "moj", "ave", "ve", "os", "ac", "ial", "al", "ey",
            "nus", "ora", "nep", "ton", "ry", "ars", "ju", "ura",
            "py", "tal", "cry", "bng", "ta", "the", "at", "we", "thy", "you", "me", "im",
            "am", "is", "are", "ger", "les", "ess", "lee", "gy", "er", "nol", "nil",
            "so", "ti", "tan", "omi", "cy", "nul", "nl", "ir", "ok", "io",
            "q","ni","kav","fsh","dra","ki","ir","ari","ya","ira","sep","bav",
            "","","","","","","","","","","","",
            "ar","chi","tra","beh","meh","ehr","aba","esf","ord","tir","var","ar",]


f = open("list.txt", "r")
listName = f.read().split(',')
f.close()


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


while True:
    while len(name) < 6:
        index = randint(0, len(listSeed) - 1)
        name += listSeed[index]

    if listName.count(name) > 0 or name[0:1] == name[1:2]:
        name = ""
        continue

    listName.append(name)
    if temp < 10:
        temp += 1
    else:
        temp = 0
        with open("list.txt", "a") as text_file:
            text_file.write(f"{name}, ")
        result = input("extract more ? (n -> no) -->> ")

        if result.count("n"):
            sys.exit()
        else:
            os.system(f"tput clear")

    max = randint(1, 100)
    for progress in range(0, 100, (100 / max).__int__()):
        os.system("tput sc")
        print(f" - - - >> {colors.BOLD}{colors.FAIL}{colors.UNDERLINE}{progress}{colors.ENDC} \
            {colors.OKBLUE}do{colors.ENDC}")
        os.system("tput rc")

    print(f"---->> {colors.BOLD}{colors.OKBLUE}{name}{colors.ENDC} \
          {colors.OKBLUE}done{colors.ENDC}")
    os.system(f"say {name}")

    name = ""
