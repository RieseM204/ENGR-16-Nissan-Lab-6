import os                                                                           # Import OS to access directories
import numpy as np                                                                  # Import NumPy for just about everything
import pandas as pd                                                                 # Import Pandas to work with the data
import math                                                                         # Import math just in case
from scipy.signal import savgol_filter                                              # Import savgol filter just in case
import lib.data_formatter as datform                                                # Import my data formatting library
import lib.trig as trig                                                             # Import my trigonometry library
import lib.phys as phys                                                             # Import my physics equation library
import matplotlib.pyplot as plt

colors = ["Green", "White", "Yellow"]

def test():
    for color in colors:
        df = pd.read_csv(f"bin/{color}_Spring.csv")
        df = df.dropna(axis = "index", how = "any")
        pos_x = df["position_px_x-hotpink"].tolist()
        pos_y = df["position_px_y-hotpink"].tolist()
        ts = df["timestamp"].tolist()
        print(f"{color} pos_x: {pos_x}")
        print(f"{color} pos_y: {pos_y}")
        print(f"{color} timestamp: {ts}")
    raise NotImplementedError

if __name__ == "__main__":                                                        # Boilerplate to show that this is the main file
    test()
    pass