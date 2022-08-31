from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
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


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()

