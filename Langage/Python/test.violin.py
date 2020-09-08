import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
n_datasets = 10
n_samples = 730
data = np.random.randn(n_datasets,n_samples)
data = [1,1,1,1,0,0,0]
data2 = data


boxname = ['Original', 'Predit']
data = [np.array(data), np.array(data2)]
_, axes = plt.subplots(figsize=(15, 10))
sns.violinplot(ax=axes, data=data, fontsize=15)
pylab.xticks([0, 1], boxname, fontsize=15)
plt.title('Distribution des probabilités d etre une protéine native', fontsize=20)
plt.savefig('violin.png')
