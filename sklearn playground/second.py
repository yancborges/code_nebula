import imp

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import svm
from matplotlib import style
style.use("ggplot")

x1 = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])

y1 = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', C=1.0)

clf.fit(x1,y1)
print(clf.predict([[10.58,10.76]]))

w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a*xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(x1[:, 0], x1[:,1], c=y1)
plt.legend()
plt.show()