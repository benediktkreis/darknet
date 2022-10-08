#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Plotting training result
fig = plt.figure(figsize=(10,10))
train_result = plt.imread("chart.png")
plt.axis(False)
plt.imshow(train_result)