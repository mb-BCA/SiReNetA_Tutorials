"""This module defines a few specs to control and unify the visualization of
plots and behaviour of Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the default scale for the plots
plt.rcParams['figure.dpi'] = 72
# Define the sizes of the lables and titles in the plots
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.frameon'] = False

# Define the colors for the plots later
std_cols = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf' ]
new_cols = ['deepskyblue', '#1f77b4', 'red', '#d62728']

# Define a new "BwR", "Blues" and "Reds" colormaps
from matplotlib.colors import ListedColormap
new_cmap = np.genfromtxt('../Data/Matplotlib_colormap_div.csv', delimiter=',')
new_bwr = ListedColormap(new_cmap)
new_Reds = ListedColormap(new_cmap[128:, :])
new_Blues = ListedColormap(new_cmap[:128, :])
