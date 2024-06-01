import numpy as np
import matplotlib.pyplot as plt


class Object(object):
    def __init__(self, coordinates: np.array):
        self.coordinates = coordinates

    def print_object(self, coordinates: np.array):
        x = coordinates[:, 0]
        y = coordinates[:, 1]
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, marker='o')
        plt.fill(x, y, alpha=0.3, color='orange')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()

    def rotate(self, angle: float):
        angle = np.radians(angle)
        rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        new_coordinates = self.coordinates @ rotation
        self.print_object(new_coordinates)

    def __str__(self):
        self.print_object(self.coordinates)

batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8],
                   [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
batman_object = Object(batman)
batman_object.rotate(30)

