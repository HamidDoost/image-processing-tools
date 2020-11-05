'''
===============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 01/11/2020
-- Description:	This code is for T-distributed Stochastic Neighbor Embedding (t-SNE) 
                which is a method for redcuing dimension for image comparison.
                This can be used for visualisation of correlation or connection 
                between images belong to a unit class.
-- Status:      In progress
===============================================================================
'''

import numpy as np
import cv2
import sys
import os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def image_to_feature_vector(image, size=(16, 16)):
    return cv2.resize(image, size).flatten()


data = []
labels = []


for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        ext = filename[filename.rfind("."):].lower()
        imagePath = os.path.join(root, filename)
        label = imagePath.split(os.path.sep)[-2]
        print(label)
        image = cv2.imread(imagePath, 0)
        H = image_to_feature_vector(image, size=(160, 160))
        H = np.array(H, dtype="float") / 255.0
        labels.append(label)
        data.append(H)


data = np.array(data)
tsne = TSNE(n_components=2, random_state=0)
X = data
X_2d = tsne.fit_transform(X)

plt.figure(figsize=(6, 5))
colors = 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple'
y = []
la = list(set(labels))
print(la)
for i in range(0, len(X)):
    for j in range(0, len(la)):
        if labels[i] == la[j]:
            y.append(j)
            plt.scatter(X_2d[i, 0], X_2d[i, 1], c=colors[j], label=la[j])

            break
plt.show()
