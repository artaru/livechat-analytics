from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from Recorder import Recorder


def filterBadWords(badWords, message):
    # Write your code here
    bad = badWords.split(" ")
    mes = message.split(" ")
    for i in range(len(bad)):
        if bad[i][-1] == "*" and bad[i][0] == "*":
            for o in range(len(mes)):
                if bad[i][1:-1] in mes[o]:
                    for l in mes[o]:
                        if l.isalpha():
                            mes[o] = mes[o].replace(l, "*")
        elif bad[i][-1] == "*":
            for o in range(len(mes)):
                if bad[i][0:-1] == mes[o][0:len(bad[i])-1]:
                    rep = ""
                    for l in mes[o]:
                        if l.isalpha():
                            rep += "*"
                    mes[o] = rep+mes[o][len(rep):]
        elif bad[i][0] == "*":
            for o in range(len(mes)):
                if bad[i][1:] == mes[o][-len(bad[i])+1:]:
                    rep = ""
                    for l in mes[o]:
                        if l.isalpha():
                            rep += "*"
                    mes[o] = rep+mes[o][len(rep):]
        else:
            for o in range(len(mes)):
                if bad[i] == mes[o]:
                    for l in mes[o]:
                        if l.isalpha():
                            mes[o] = mes[o].replace(l, "*")
    return " ".join(mes)


if __name__ == '__main__':
    a = Recorder()
    a.record([0.1, 0.3, 0.5])
