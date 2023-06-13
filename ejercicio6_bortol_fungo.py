from decimal import Decimal, getcontext

from export_data import add_row_to_csv, init_csv_file, create_filename

getcontext().prec = 7

STEP = Decimal('0.0001')
MIN_HEIGHT = 0.00001
MAX_T = 100
THROW_HEIGHT = 10

ba = 0.1
m = 1
b = 30
g = 9.8
k = 100000


def calculate_next_height(previous_height, previous_velocity):
    return float(STEP) * previous_velocity + previous_height


def calculate_next_velocity(previous_velocity, previous_acceleration):
    return float(STEP) * previous_acceleration + previous_velocity


def calculate_acceleration(previous_height, previous_velocity):
    if previous_height > 0:
        return -ba / m * previous_velocity - g
    else:
        return -k * previous_height - b * previous_velocity - g


def check_change(current_height, previous_height, ascending):
    if ascending and current_height > previous_height:
        return True
    if not ascending and previous_height > current_height:
        return True
    return False


def simulate():
    t = Decimal('0')

    current_velocity = 0.0
    current_height = THROW_HEIGHT
    current_acceleration = calculate_acceleration(current_height, current_velocity)
    ascending = True

    filename = create_filename(MAX_T)
    init_csv_file(filename)

    while t < MAX_T:
        add_row_to_csv(filename, t, current_height, current_velocity, current_acceleration)
        previous_height = current_height
        current_height = calculate_next_height(current_height, current_velocity)
        current_velocity = calculate_next_velocity(current_velocity, current_acceleration)
        current_acceleration = calculate_acceleration(current_height, current_velocity)
        t += STEP
        if check_change(previous_height, current_height, ascending):
            if ascending and MIN_HEIGHT > current_height > 0:
                t = MAX_T
            ascending = not ascending


if __name__ == "__main__":
    simulate()
