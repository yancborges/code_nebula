import imp

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf =  svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)

target = -6

av = digits.data[target].reshape(1,-1)
print(av)


print('Prediction: ', clf.predict(av))

plt.imshow(digits.images[target], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
