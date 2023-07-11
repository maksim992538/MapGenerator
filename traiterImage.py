from cv2 import imread, imwrite
import numpy as np
from random import randint
from tqdm import tqdm
from time import sleep
import os
size_x=0
size_y=0
sandSeed="5009, boox1"#Песок
floorSeed="5006, planes1"#Земля
rockSeed="5006, planes1"#скала
mountain="5006, planes1"#Гора
def runperl():
    image = imread("Perling/dast.png")
    h = image.shape[0]
    map = np.zeros((h, h, 3), np.uint8)
    Datax=[-1000,-950,-900,-850,-800,-750,-700,-650,-600,-550,-500,-450,-400,-350,-300,-250,-200,-150,-100,-50,0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
    Datay=[-1000,-950,-900,-850,-800,-750,-700,-650,-600,-550,-500,-450,-400,-350,-300,-250,-200,-150,-100,-50,0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
    print(len(Datax))
    def traiterImage(type):
        if type == "desert":
            for x in range(h):
                for y in range(h):
                    if image[x, y][0] > 160: map[x, y] = [255,144,30] # eau profonde
                    elif image[x, y][0] > 130: map[x, y] = [255,144,30] # eau
                    elif image[x, y][0] > 110: map[x, y] = [118,221,252] # sable
                    elif image[x, y][0] >  80: map[x, y] = [48,161,93] # sol
                    elif image[x, y][0] >  40: map[x, y] = [39,111,78] # roche
                    elif image[x, y][0] >  20: map[x, y] = [35,81,67] # montagne
                    else                     : map[x, y] = [35,70,58] # sommets
        elif type == "glace":
            for x in range(h):
                for y in range(h):
                    
                    if   image[x, y][0] > 160: map[x, y] = [127,   0,   0] # eau profonde
                    elif image[x, y][0] > 130: map[x, y] = [255,   0,   0] # eau
                    elif image[x, y][0] > 110: map[x, y] = [255, 150, 150] # bord d'eau
                    elif image[x, y][0] >  80: map[x, y] = [255, 200, 200] # sol
                    elif image[x, y][0] >  40: map[x, y] = [190, 190, 190] # plutot haut
                    elif image[x, y][0] >  20: map[x, y] = [220, 220, 220] # haut
                    else                     : map[x, y] = [255, 255, 255] # très haut
        elif type == "enfer":
            for x in range(h):
                for y in range(h):
                    
                    if   image[x, y][0] > 160: map[x, y] = [ 32,  32, 255] # lave profonde
                    elif image[x, y][0] > 130: map[x, y] = [ 64,  64, 255] # lave
                    elif image[x, y][0] > 125: map[x, y] = [ 32,  32,  32] # sable noir
                    elif image[x, y][0] >  90: map[x, y] = [  0,  32,  64] # sol
                    elif image[x, y][0] >  55: map[x, y] = [  0,  16,  32] # forêt
                    elif image[x, y][0] >  20: map[x, y] = [ 16,  16,  16] # montagne
                    else                     : map[x, y] = [  0,   0,   0] # sommets
    tabTypes = ["desert","glace","enfer"]
    for i in range(len(tabTypes)):
        traiterImage(tabTypes[i])
        name = "cartes/" + tabTypes[i] + ".png"
        imwrite(name, map)