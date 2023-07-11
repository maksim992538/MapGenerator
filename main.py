import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import matplotlib as mpl
from traiterImage import runperl
import time
import os
from time import sleep
xpix, ypix = 150,150


def StartingFunction():
    pic = []
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.axes.get_xaxis().set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.axes.get_yaxis().set_visible(False)
    noise1 = PerlinNoise(octaves=3)
    noise2 = PerlinNoise(octaves=6)
    noise3 = PerlinNoise(octaves=12)
    noise4 = PerlinNoise(octaves=24)
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i/xpix, j/ypix])
            noise_val += 0.5 * noise2([i/xpix, j/ypix])
            noise_val += 0.25 * noise3([i/xpix, j/ypix])
            noise_val += 0.125 * noise4([i/xpix, j/ypix])
            row.append(noise_val)
        pic.append(row)
    plt.imshow(pic, cmap='gray')
    plt.savefig( 'Perling/dast.png', dpi=60,bbox_inches='tight', transparent="True", pad_inches=0)




if __name__ == "__main__":
    StartingFunction()
    runperl()