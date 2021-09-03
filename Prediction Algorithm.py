import csv
import matplotlib
import numpy as np
import sys
import random
%matplotlib inline
from matplotlib import pyplot as plt
dataset ="C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python38\\New folder\\COVID_Dataset.csv"
population="Population.csv"

list1=[]
with open(dataset, 'r') as data:
    for line in csv.DictReader(data): 
        list1.append(line)

xlocation,ylocation=[],[]

for value in list1:
    xlocation.append(int(value['x location']))
    ylocation.append(int(value['y location']))

def distance_2d(x_point, y_point, x, y):
    return np.hypot(x-x_point, y-y_point)

ys, xs = np.ogrid[1:20:100j, 1:20:100j]
distances = distance_2d(xlocation[random.randint(0,len(xlocation))],ylocation[random.randint(0,len(ylocation))], xs, ys)
plt.figure()
plt.title('')
plt.imshow(distances, origin='lower', interpolation="none")
plt.xticks(np.arange(xs.shape[1]), xs.ravel())
plt.yticks(np.arange(ys.shape[0]), ys.ravel())
plt.axis('off')
plt.colorbar()