from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd


getcontext().prec = 7

STEP =  Decimal('0.0001')
MIN_HEIGHT = 0.00001
MAX_T = 10

ba = 0.1
m = 1
b = 30
g = 9.8
k = 100000




def calculate_next_height(previously_height, previously_velocity):
    return float(STEP) * previously_velocity + previously_height
    

def calculate_next_velocity(previously_velocity, previously_aceleration):
    return float(STEP) * previously_aceleration + previously_velocity


def calculate_aceleration(previously_height, previously_velocity):
    if(previously_height > 0):        
        return -ba / m * previously_velocity - g
    else:
        return -k * previously_height - ba * previously_velocity - g


def generateData():
    t = Decimal('0')

    previously_velocity = 0.0
    previously_height = 10
    previously_aceleration = calculate_aceleration(previously_height, previously_velocity)
    data = {'time': float(t), 'height': previously_height, 'velocity': previously_velocity, 'aceleration': previously_aceleration}
    df = pd.DataFrame(data, index=[0])
    df.to_csv('data.csv', index=False)
    while t < MAX_T:
        previously_height =  calculate_next_height(previously_height, previously_velocity)
        previously_velocity = calculate_next_velocity(previously_velocity, previously_aceleration)
        previously_aceleration = calculate_aceleration(previously_height, previously_velocity)
        data = {'time': float(t), 'height': previously_height, 'velocity': previously_velocity, 'aceleration': previously_aceleration}
        df = pd.DataFrame(data, index=[0])
        df.to_csv('data.csv', mode='a', header=False, index=False)
        t += STEP



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
    # generateData()
    plot_data()

if __name__ == "__main__":
    main()
    # generateData()

def check_heights_min(t, height):
    if(heights.__contains__(t-STEP*Decimal(2)) and heights.__contains__(t-STEP)):
        if heights[t-STEP*Decimal(2)] < heights[t-STEP] and height < heights[t-STEP]:
            if heights[t-STEP] <= MIN_HEIGHT:
                return True
    return False


