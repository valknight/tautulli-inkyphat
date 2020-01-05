
from tautulli_reader import get_play_count
import matplotlib.pyplot as plt
import pandas as pd
import os
aspect_ratio = 212/104


def play_count_graph(days=7):
    # get data from tautulli
    play_count = get_play_count(days=days)
    data = play_count['resp']['data']
    x_data = []
    y_data = []
    day_count = 0
    for day in data['categories']:
        x_data.append(0 - day_count)
        y_data.append(0)
        day_count += 1
    # we do this as appending doesn't work great
    x_data.reverse()
    # this merges all datapoints we have
    for series in data['series']:
        for x in range(0, len(series['data'])):
            y_data[x] += series['data'][x]
    generate_graph("play_count", x_data, y_data)


def generate_graph(graph_name, x_data, y_data):
    fig, ax = plt.subplots()
    fig.set_size_inches(aspect_ratio*1.5, 1.5)
    ax.plot(x_data, y_data, color="black")
    ax.xaxis.set_visible(False)
    plt.grid()
    if not os.path.exists("images"):
        os.mkdir("images")
    fig.savefig("images/{}.png".format(graph_name),
                bbox_inches='tight', pad_inches=0)


if __name__ == '__main__':
    play_count_graph()
