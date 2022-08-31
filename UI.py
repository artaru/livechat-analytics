from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_image
from Collector import Collector
from Recorder import Recorder
import pandas as pd
import matplotlib.pyplot as plt
import time
import io
from PIL import Image
from pywebio.input import *
from matplotlib.animation import FuncAnimation


def animate(i):
    mylabels = ["Negative", "Neutral", "Positive"]
    data = pd.read_csv('data.csv')
    plt.style.use('fivethirtyeight')
    y1 = 0
    y2 = 0
    y3 = 0
    if len(data.values.tolist()) >= 5:
        y = data.values.tolist()[-5:]
        for i in y:
            y1 += i[0]
            y2 += i[1]
            y3 += i[2]
        plt.cla()

        plt.pie([y1, y2, y3], labels=mylabels)
        plt.legend(loc='upper left')
        plt.tight_layout()


def plot(link, num):
    c = Collector(link)
    r = Recorder()
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.tight_layout()
    plt.show()
    while True:
        r.record(c.analytics(num))


def menu():
    link = input("Link：", type=TEXT)
    num = input("Batch size for analysis：", type=FLOAT)
    plot(link, num)


if __name__ == '__main__':
    menu()
