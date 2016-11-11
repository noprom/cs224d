# coding=utf-8
'''
@Title:Simple SVD word vectors in Python

@Author: tyee.noprom@qq.com
@Time: 11/11/2016 3:15 PM
'''
import numpy as np
import matplotlib.pyplot as plt

la = np.linalg
words = ["I", "like", "enjoy",
         "deep", "learning", "NLP", "flying", "."]
X = np.array([[0, 2, 1, 0, 0, 0, 0, 0],
              [2, 0, 0, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 1, 1, 0]])

U, s, Vh = la.svd(X, full_matrices=False)
fig = plt.figure()
fig.suptitle('Simple SVD word vectors in Python', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

ax.plot([2], [1], 'o')
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
for i in xrange(len(words)):
    ax.text(U[i, 0], U[i, 1], words[i])

ax.axis([-0.8, 0.2, -0.8, 0.8])
plt.show()
