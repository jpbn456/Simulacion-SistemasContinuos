from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

getcontext().prec = 4

STEP =  Decimal('0.001')
MIN_HEIGHT = 0.00001
MAX_T = 10

heights = {Decimal('0'): 10}
velocities = {Decimal('0'): 0}
accelerations = {}



def height(t):
    if(t <= Decimal('0')): return heights[Decimal('0')]
    if not heights.__contains__(t):
        h = float(STEP) * float(velocity(t - STEP)) + height(t - STEP)
        if h <= MIN_HEIGHT: return 0
        heights.update({t: h})  
    return heights[t]


def velocity(t):
    if(t <= Decimal('0')): return velocities[Decimal('0')]
    if not velocities.__contains__(t):
        velocities.update({t: float(STEP) * acceleration(t - STEP) + velocity(t - STEP)})
    return velocities[t]


def acceleration(t):
    if not accelerations.__contains__(t):
        if(height(t) > 0):
            accelerations.update({t: -0.1 * velocity(t)-9.8})
        else:
            accelerations.update({t: -100000 * height(t) - 0.1 * velocity(t) - 9.8})
    return accelerations[t]

    
def generateData():
    max_height_reached = False
    t = Decimal('0')
    partial_height = -9999
    height_list = []
    velocity_list = []

    while(partial_height != 0):
        partial_height = height(Decimal(str(t)))
        height_list.append(partial_height)
        velocity_list.append(velocity(t))
        t += STEP
    # print(height_list)
    times = [i * 0.0001 for i in range(len(height_list))]

    plt.plot(times, height_list)
    plt.xlabel('Tiempo')
    plt.ylabel('Altura')
    plt.title('Gráfico de alturas en función del tiempo')
    plt.grid(True)
    plt.show()
    # print(velocity_list)

if __name__ == "__main__":
    generateData()
   
