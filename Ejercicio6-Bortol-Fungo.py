from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd

getcontext().prec = 7

STEP = Decimal('0.001')
MIN_HEIGHT = 0.00001
MAX_T = 100

ba = 0.1
m = 1
b = 30
g = 9.8
k = 10000


def calculate_next_height(previous_height, previous_velocity):
    return float(STEP) * previous_velocity + previous_height


def calculate_next_velocity(previous_velocity, previous_acceleration):
    return float(STEP) * previous_acceleration + previous_velocity


def calculate_acceleration(previous_height, previous_velocity):
    if previous_height > 0:
        return -ba / m * previous_velocity - g
    else:
        return -k * previous_height - ba * previous_velocity - g


def check_change(current_height, previous_height, ascending):
    if ascending and current_height < previous_height:
        return True
    if not ascending and previous_height < current_height:
        return True
    return False


def generateData():
    t = Decimal('0')
    previous_velocity = 0.0
    previous_height = 10
    previous_acceleration = calculate_acceleration(previous_height, previous_velocity)
    ascending = False
    data = {'time': float(t), 'height': previous_height, 'velocity': previous_velocity,
            'acceleration': previous_acceleration}
    df = pd.DataFrame(data, index=[0])
    df.to_csv('data.csv', index=False)
    while t < MAX_T:
        current_height = previous_height  # Implementing
        previous_height = calculate_next_height(previous_height, previous_velocity)
        previous_velocity = calculate_next_velocity(previous_velocity, previous_acceleration)
        previous_acceleration = calculate_acceleration(previous_height, previous_velocity)

        data = {'time': float(t), 'height': previous_height, 'velocity': previous_velocity,
                'acceleration': previous_acceleration}
        df = pd.DataFrame(data, index=[0])
        df.to_csv('data.csv', mode='a', header=False, index=False)
        t += STEP
        if check_change(current_height, previous_height, ascending):
            if ascending and MIN_HEIGHT > current_height > 0:
                t = MAX_T
            ascending = not ascending


def plot_data():
    data = pd.read_csv('data.csv')
    time = data['time']
    height = data['height']
    velocity = data['velocity']
    plt.plot(time, height)
    plt.xlabel('Tiempo')
    plt.ylabel('Altura')
    plt.title('Gráfico de alturas en función del tiempo')
    plt.grid(True)
    plt.show()

    plt.plot(time, velocity)
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title('Gráfico de velocidades en función del tiempo')
    plt.grid(True)
    plt.show()


def main():
    generateData()
    plot_data()


if __name__ == "__main__":
    main()
    # generateData()
