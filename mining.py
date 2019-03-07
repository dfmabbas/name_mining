import os
import time
from random import randint
import random


os.system("clear")

listName = []
name = ""
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
            "so", "ti", "tan", "omi", "cy", "nul", "nl", "xi",
            "ko", "qx", "xq", "ir", "ok", "dar", "sam"]


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
    with open("list.txt", "a") as text_file:
        text_file.write(f"{name}, ")

    max = randint(1, 100)
    for progress in range(0, max, (100 / max).__int__()):
        os.system("tput sc")
        print(f" - - >> {colors.BOLD}{colors.FAIL}{colors.UNDERLINE}{progress}{colors.ENDC} \
              {colors.OKBLUE}...{colors.ENDC}")
        os.system("tput rc")
        os.system("tput ed")

    os.system("tput rc")
    os.system("tput ed")
    print(f"---->> {colors.BOLD}{colors.OKBLUE}{name}{colors.ENDC}")
    os.system(f"say {name}")

    name = ""
