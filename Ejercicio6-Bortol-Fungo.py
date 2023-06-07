STEP = 0.0001
MIN_HEIGHT = 0.00001
MAX_T = 100

heights = {0: 0}
velocities = {0: 0}
accelerations = {}



def height(t):
    print(" heights \n" + str(heights))
    print("Time H = "+ str(t))
    if not heights.__contains__(t):
        heights[t] =  STEP * velocity(t - STEP) + height(t - STEP)
    return heights[t]


def velocity(t):
    print(" velocities \n" + str(velocities))
    print("Time V = "+ str(t))
    if not velocities.__contains__(t):
        velocities[t] =  STEP * acceleration(t - STEP) + velocity(t - STEP)
    return velocities[t]


def acceleration(t):
    # print(str(t))
    print(" acceleration \n" + str(accelerations))
    print("Time A = "+ str(t))
    if not accelerations.__contains__(t):
        if(height(t) > 0):
            accelerations[t] = -0.1 * velocity(t)-9.8
        else:
            accelerations[t] = -100000 * height(t) - 0.1 * velocity(t) - 9.8
    return accelerations[t]

    
def generateData():
    max_height_reached = False
    t = 0
    partial_height = 0
    a = acceleration(0.0003)
    print(a)
	#while(t < MAX_T and not max_height_reached):
    #    partial_height = height(t)
    #    if(partial_height >= MAX_HEIGHT):
    #        max_height_reached = True
    #    height_list.append(partial_height)
    #    velocity_list.append(velocity(t))
    #    t += STEP
    #print(height_list)
    #print(velocity_list)

if __name__ == "__main__":
    generateData()
   
