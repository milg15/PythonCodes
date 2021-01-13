import pandas as pd
import matplotlib.pyplot as plt, mpld3
from mpld3 import plugins, utils
import numpy as np

""" calories,protein,fat,carbo """
data = pd.read_csv("cereal.csv")
replace = {r'Q': 1, 'K': 2, 'R': 3, 'P': 4, 'N': 5, 'G': 6, 'A': 7}

X = data[['calories', 'protein', 'fat','carbo']].to_numpy()
y = np.concatenate(data[['mfr']]
    .replace(regex=replace).to_numpy())
# dither the data for clearer plotting
X += 0.1 * np.random.random(X.shape)

fig, ax = plt.subplots(4, 4, sharex="col", sharey="row", figsize=(10, 10))
fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95,
                    hspace=0.1, wspace=0.1)

for i in range(4):
    for j in range(4):
        points = ax[3 - i, j].scatter(X[:, j], X[:, i],
                                      c=y, s=40, alpha=0.6)

# remove tick labels
for axi in ax.flat:
    for axis in [axi.xaxis, axi.yaxis]:
        axis.set_major_formatter(plt.NullFormatter())


# Here we connect the linked brush plugin
plugins.connect(fig, plugins.LinkedBrush(points))

f = open('index.html', 'w+')
f.write(mpld3.fig_to_html(fig))
f.close()
