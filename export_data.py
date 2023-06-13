import os

import pandas as pd
import csv


def create_filename(max_t):
    base_filename = f"data_{max_t}_tries.csv"
    filename = base_filename
    counter = 1

    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}"
        counter += 1

    return filename


def init_csv_file(filename):
    header = ['time', 'height', 'velocity', 'acceleration']  # Replace with your actual column names
    # with open('your_file.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header)


def add_row_to_csv(filename, time, height, velocity, acceleration):
    data = {'time': float(time), 'height': height, 'velocity': velocity, 'acceleration': acceleration}
    df = pd.DataFrame(data, index=[0])

    if not os.path.isfile(filename):
        df.to_csv(filename, header=True, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)
