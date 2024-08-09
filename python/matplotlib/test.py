#!/usr/bin/env python3

import numpy as np
from tabulate import tabulate
from matplotlib import pyplot as plt


def display_common_angle_names():
    headers=['Angle', 'Degrees', 'Radians (π)', 'Radians (~#)']
    values=[
        ['0° or Zero', '0', '0', '0'],
        ['Acute', '0 < θ < 90', '0 < θ < π/2', '0 < θ < 1.57'],
        ['Right', '90', 'π/2', '1.57'],
        ['Obtuse', '90 < θ < 180', 'π/2 < θ < π', '1.57 < θ < 3.14'],
        ['Straight', '180', 'π', '3.14'],
        ['Reflex', '180 < θ < 360', 'π < θ < 2π', '3.14 < θ < 6.28'],
        ['360° or Complete', '360', '2π', '6.28'],
    ]
    colalign=['left', 'right', 'right', 'right']
    print(tabulate(values, headers=headers, colalign=colalign))


def plot():
    xs = np.linspace(-2*np.pi, 2*np.pi, 100)
    ys = np.sin(xs)
    plt.plot(xs, ys)
    plt.show()


def main(args=None):
    display_common_angle_names()
    plot()
    

if __name__ == "__main__":
    main()
