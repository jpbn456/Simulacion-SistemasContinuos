import pandas as pd
import matplotlib.pyplot as plt
import sys


def plot_csv(filename):
    df = pd.read_csv(filename)
    time = df['time']
    height = df['height']
    velocity = df['velocity']
    plt.plot(time, height)
    plt.plot(time[0], height[0], 'ro')
    plt.xlabel('Tiempo')
    plt.ylabel('Altura')
    plt.title('Gráfico de alturas en función del tiempo')
    plt.grid(True)
    plt.show()
    plt.plot(time, velocity)
    plt.plot(time[0], velocity[0], 'ro')
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title('Gráfico de velocidades en función del tiempo')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    plot_csv(sys.argv[1])
