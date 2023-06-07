STEP = 0.0001
MAX_HEIGHT = 0.00001
MAX_T = 1

height_list = []
velocity_list = []


def height(t):
    if(t == 0):
        return 0
    else:
        return height(t - STEP) + velocity(t) * STEP

def velocity(t):
    if (t == 0):
        return 0
    else:
        return velocity(t - STEP) + acceleration(t) * STEP


def acceleration(t):
    if(height(t) > 0):
        return -0.1 * velocity(t)-9.8
    else:
        return -100000 * height(t) - 0.1 * velocity(t) - 9.8
    
def generateData():
    max_height_reached = False
    t = 0
    partial_height = 0
    while(t < MAX_T and not max_height_reached):
        partial_height = height(t)
        if(partial_height >= MAX_HEIGHT):
            max_height_reached = True
        height_list.append(partial_height)
        velocity_list.append(velocity(t))
        t += STEP
    print(height_list)
    print(velocity_list)

if __name__ == "__main__":
    generateData()
   