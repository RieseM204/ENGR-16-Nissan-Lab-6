import numpy as np                                                                  # Import NumPy for just about everything
import pandas as pd                                                                 # Import Pandas to work with the data
import math                                                                         # Import math for... math
import matplotlib.pyplot as plt

colors = ["Green", "White", "Yellow"]

m = 0.2

def main():
    for color in colors:
        # level 0: importing data for a given color and formatting what i need
        df = pd.read_csv(f"bin/{color}_Spring.csv")
        df = df.dropna(axis = "index", how = "any")
        pos_x = df["position_px_x-hotpink"].tolist()
        pos_y = df["position_px_y-hotpink"].tolist()
        ts = df["timestamp"].tolist()

        # level 1: basic data processing
        x_int = np.mean(pos_x[0:151]) # resting position
        pos_x = [i - x_int for i in pos_x] # translating the positions to be centered on the resting position


        rest_ts = []    # calculating the time stamps of peaks
        for t in range(len(pos_x[1:-1])):
            if pos_x[t] > pos_x[t-1] and pos_x[t] > pos_x[t+1]:
                rest_ts.append(float(ts[t]))
        
        p_list = []     # calculating the period between each peak
        for t in range(len(rest_ts[:-1])):
            p_diff = rest_ts[t+1] - rest_ts[t]
            p_list.append(float(p_diff))
        p = np.mean(p_list)
   
        # level 2: useful data
        T = p/1000 # period in seconds
        ang_freq = (2 * math.pi)/T # angular frequency
        k = (ang_freq ** 2) * m # spring constant
        print(f"{color} spring constant: {k}")

        # plotting
        plt.plot(ts[300:], pos_x[300:])
        plt.axhline(color = 'red')
        plt.title(f"{color} Spring Vertical Position vs. Time")
        plt.xlabel("Time (ms)")
        plt.ylabel("Vertical Position (px)")
        plt.show()

if __name__ == "__main__":                                                        # Boilerplate to show that this is the main file
    main()