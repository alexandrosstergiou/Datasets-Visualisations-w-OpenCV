import cv2
import numpy as np
import os


def stack_dataset_examples(directory):

    l = []
    for item in os.listdir(directory):
        if not item.startswith('.'):
            l.append(item)

    l = sorted(l)

    images = []

    for li in l:
        
        li = directory+"/"+li
        temp = cv2.imread(li)
        temp = cv2.resize(temp,(700,450))
        images.append(temp)

    numpy_horizontal1 = np.hstack((images[0], images[1], images[2], images[3]))
    numpy_horizontal2 = np.hstack((images[4], images[5], images[6], images[7]))

    numpy_horizontal = np.vstack((numpy_horizontal1, numpy_horizontal2))

    return numpy_horizontal

directories= []
for item in os.listdir('.'):
    if not item.startswith('.') and not os.path.isfile(os.path.join('.', item)):
        directories.append(item)

directories=sorted(directories)
stacked_images = []
for d in directories:
    stacked_images.append(stack_dataset_examples(d))

cluster_imgs = []
for i in range(0,len(stacked_images),3):
    if i+1>len(stacked_images):
        cluster_imgs.append(stacked_images[i])
    elif i+2>len(stacked_images):
        cluster_imgs.append(np.hstack((stacked_images[i], stacked_images[i+1])))
    else:
        cluster_imgs.append(np.hstack((stacked_images[i], stacked_images[i+1], stacked_images[i+2])))

fin_image = np.vstack(cluster_imgs)
cv2.imwrite("Figure.png",fin_image)
