# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:52:33 2019

@author: Jinfen Zhang
Edit by Bruce

"""
import numpy as np
import GetVoPolygons as gvp
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


def PolygonTransform(polygon):
    #把shapely.geometry中的Polygon格式转换成matplotlib格式的Polygon
    x, y = polygon.exterior.coords.xy
#    print(x)
    len_x = len(x)
    polygon_transform = []
    for i in np.arange(len_x):
        point_temp = [x[i],y[i]]
        polygon_transform.append(point_temp)
    polygon_transform = Polygon(polygon_transform, True)
    return polygon_transform


def GenVOImg(pos1, course1, speed1, pos2, course2, speed2, ImgID):
    """ 
    绘制并生成VO图 .
    生成的VO图存储在 "/res/VOImg/" 路径下.
    图片名称格式为 XXXX.png 其中XXXX为ImgID, 也即是虚拟机下某个船舶对应某次运行的ID.
    """
    fig, ax = plt.subplots()

    poly_vo,poly_front,poly_rear,poly_diverging = gvp.GetVoPolygons(pos1,course1,speed1,pos2,course2,speed2)

    patches = []
    colors = []
    if poly_vo:
        poly_vo = PolygonTransform(poly_vo)
        patches.append(poly_vo)
        colors.append(10)
        
    if poly_front:
        poly_front = PolygonTransform(poly_front)
        patches.append(poly_front)
        colors.append(30)

    if poly_rear:
        poly_rear = PolygonTransform(poly_rear)
        patches.append(poly_rear)
        colors.append(50)

    if poly_diverging:
        poly_diverging = PolygonTransform(poly_diverging)
        patches.append(poly_diverging)
        colors.append(70)
    # print(colors)
    #
    # fig, ax = plt.subplots()
    p = PatchCollection(patches, alpha=0.4)
    ax.add_collection(p)

    p.set_array(np.array(colors))
    ax.add_collection(p)

    #画速度向量
    vx = speed1 * 500 * np.sin(course1 * np.pi / 180)
    vy = speed1 * 500 * np.cos(course1 * np.pi / 180)
    ax.arrow(pos1[0], pos1[1], vx, vy, length_includes_head=True,\
            head_width=200, head_length=400, fc='r', ec='r')

    plt.xlim(pos1[0]-4000, pos1[0]+4000)
    plt.ylim(pos1[1], pos1[1]+8000)

    # plt.ion()
    # plt.plot()
    # plt.pause(1)
    # plt.cla()
    plt.savefig("./res/VOImg/{}.png".format(str(ImgID)))
    # plt.show()
    print('[DrawVoAreas]: Call DrawVoAreas succeed & VO Img {}.png saved.'.format(str(ImgID)))
    pass


# 使用这里的数值测试，course就是ship的heading,即航艏向
# pos1 = [1000,-5134]
# course1 = 0
# speed1 = 5.144

# pos2 = [1950,1964]
# course2 = 180
# speed2 = 5.144

# def main():
#     GenVOImg(pos1, course1, speed1, pos2, course2, speed2, 1000010086)
#     pass


# if __name__ == '__main__':
#     main()
    