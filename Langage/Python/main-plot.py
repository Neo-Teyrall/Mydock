import matplotlib
import matplotlib.pyplot as plt

a = plt.plot([1,2],[2,3])
#plt.show()

plt.close()
plt.plot([1,2],[4,5])
plt.legend(["oui"], prop={'size': 12}) 
plt.savefig("here.png")


import tensorflow as tf
a = tf.keras.Sequential()
a.

