import random
import numpy as np
import matplotlib.pyplot as plt
img = plt.imread('picture.jpg')  #导入图片数据
shape = img.shape
#plt.imshow(img)
#plt.show()
K = 20  #聚类个数
iteration = 5  #最大迭代次数
center = []  #聚类颜色中心位置，RGB三元组
label = [[-1 for j in range(0, 256)] for i in range(0, 256)]  #类别号（标签）
distance = [[[0 for z in range(K)]for j in range(0, 256)] for i in range(0, 256)]
#各图像点到不同聚类中心的距离
def randcenter():  #生成初始聚类中心位置
    center.append(img[random.randint(0, shape[0] - 1), random.randint(0, shape[1] - 1)])
    for i in range(1, K):
        while 1:  #确保聚类中心不同
            color = img[random.randint(0, shape[0] - 1), random.randint(0, shape[1] - 1)]
            flag = 1  #无重复为1，重复为0
            for j in range(i):
                if (color == center[j]).all():
                    flag = 0
                    break
            if flag == 1:  #无重复则跳出，追加写入
                break
        center.append(color)
    return 0


def cal_distance():
    for i in range(shape[0]):
        for j in range(shape[1]):
            for z in range(K):
                distance[i][j][z] = (int(img[i][j][0]) - center[z][0])**2 + \
                                    (int(img[i][j][1]) - center[z][1])**2 + \
                                    (int(img[i][j][2]) - center[z][2])**2
                #print(distance[i][j][z])
    return 0


def cal_label():
    for i in range(shape[0]):
        for j in range(shape[1]):
            min = 196608
            for z in range(K):
                if distance[i][j][z] < min:
                    min = distance[i][j][z]
                    label[i][j] = z
    return 0


def cal_center():
    sum = [[0, 0, 0]for i in range(K)]
    count = [0 for i in range(K)]  #统计第K类有多少个
    for i in range(shape[0]):
        for j in range(shape[1]):
            count[label[i][j]] += 1
            sum[label[i][j]][0] += int(img[i][j][0])
            sum[label[i][j]][1] += int(img[i][j][1])
            sum[label[i][j]][2] += int(img[i][j][2])
    for i in range(K):
        center[i][0] = sum[i][0] / count[i]
        center[i][1] = sum[i][1] / count[i]
        center[i][2] = sum[i][2] / count[i]
    return 0


def K_means():
    randcenter()
    index = 0  #初始迭代次数
    while True:
        old_center = center
        cal_distance()  #计算distance
        cal_label()  #计算标签label
        cal_center()  #算出新的中心点center
        index += 1
        print('当前迭代次数为：', index)
        if index > iteration or old_center == center:
            break
    print('最终迭代次数为：', index)
    return 0


def change_img():
    for i in range(shape[0]):
        for j in range(shape[1]):
            img[i][j] = center[label[i][j]]
    return 0


K_means()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#plt.subplot(121), plt.title("原图像")
#plt.imshow(img)
change_img()
#plt.subplot(122), plt.title("K_means分类数10")
plt.imshow(img)
plt.title("K_means分类数20")
plt.show()

