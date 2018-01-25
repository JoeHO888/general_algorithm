import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)


def F(array):
  return 2*np.sin(array)+np.cos(array)

pop=np.linspace(0,5,10)

ax.plot(pop,F(pop),"ro")
fig.savefig('graph.png')
