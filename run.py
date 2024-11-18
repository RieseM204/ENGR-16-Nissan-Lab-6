import os                                                                           # Import OS to access directories
import numpy as np                                                                  # Import NumPy for just about everything
import pandas as pd                                                                 # Import Pandas to work with the data
import math                                                                         # Import math just in case
from scipy.signal import savgol_filter                                              # Import savgol filter just in case
import lib.data_formatter as datform                                                # Import my data formatting library
import lib.trig as trig                                                             # Import my trigonometry library
import lib.phys as phys                                                             # Import my physics equation library
import matplotlib.pyplot as plt