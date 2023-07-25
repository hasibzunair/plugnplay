import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""Plots a graph for two methods and point chart to compare many methods."""

sns.set()
sns.set(font_scale=1.2)
plt.rcParams['figure.figsize'] = (7,5)
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
#plt.rcParams['font.family'] = 'Times New Roman'
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42
np.random.seed(1)

# Plot graph
fig = plt.figure()
alpha = [0.05, 0.1, 0.12, 0.15, 0.17, 0.2, 0.25, 0.3, 0.4, 0.5]
MPJPE = [39.79, 38.63, 38.27, 39.99, 38.94, 38.64, 40.79, 40.72, 41.08, 42.60]
PAMPJPE = [31.48, 30.41, 30.51, 30.96, 30.75, 31.06, 32.14, 32.53, 31.85, 33.66]
plt.plot(alpha, MPJPE, 'ro-', label='Method 1', lw=2)
plt.plot(alpha, PAMPJPE, 'bs-', label='Method 2', lw=2)
plt.legend(loc='best')
plt.xlabel(r'$\alpha$', fontsize=15)
plt.ylabel(r'Evaluation Metric (mm)', fontsize=15)
plt.savefig('./graph.pdf', format='PDF', dpi=300, bbox_inches='tight')


# Plot point chart to compare methods
fig = plt.figure()
x = np.array([0.43, .63, 0.76, 1.1, 1.2, 4.2, 3.7])
y = np.array([40.78,36.34,34.83, 37.43,39.52,37.83, 38.1])
n = ['Sem-GCN','Ours','Ours (§)','Modulated GCN','Higher Order GCN','Weight Unsharing','Local-to-Global Net (§)']
colors = np.random.rand(7)

#plt.scatter(x, y, c=colors)
#plt.legend(loc='best')
plt.xlabel(r'Parameters', fontsize=15)
plt.ylabel(r'MPJPE (mm)', fontsize=15)

plt.annotate(n[0], (x[0]+.15,y[0]-.12))
plt.annotate(n[1], (x[1]+.15, y[1]-.12))
plt.annotate(n[2], (x[2]+.15, y[2]-.12))
plt.annotate(n[3], (x[3]+.15, y[3]-.13))
plt.annotate(n[4], (x[4]+.15, y[4]-.04))
plt.annotate(n[5], (x[5]-.8,y[5]-.5))
plt.annotate(n[6], (x[6]-.7,y[6]+.2))

plt.scatter(x = x[0],y=y[0], marker='s',s = 100)
plt.scatter(x = x[1],y=y[1], marker='*',s=150)
plt.scatter(x = x[2],y=y[2], marker='*',s=150)
plt.scatter(x = x[3],y=y[3], marker='^',s=100)
plt.scatter(x = x[4],y=y[4], marker=7,s=100)
plt.scatter(x = x[5],y=y[5], marker='o',s=100)
plt.scatter(x = x[6],y=y[6], marker='H',s=100)

ax = plt.gca()
#ax.set_xlim(xmax=5.0)
#ax.set_xlim([0,5.0])
ax.set_ylim([34, 42])

x_labels = [.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
x_ticks = [.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]

#add x-axis values to plot
plt.xticks(ticks=x_ticks, labels=x_labels)

#plt.show()
plt.savefig('./pointplot.pdf', format='PDF', dpi=300, bbox_inches='tight')