import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')

# plt.figure(2)                # a second figure
# plt.plot([1, 2, 3])
# plt.legend(['A simple line'])

# plt.figure(3)
# plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
# plt.plot([1,2,3], [1,4,9], 'rs',  label='line 2')
# plt.plot([1,2,3], [1,5,9], 'c+:',  label='line 3')
# plt.plot([1,2,3], [1,6,9], 'b.-',  label='line 4')
# plt.axis([0, 4, 0, 10])
# plt.legend()

# plt.figure(4)
# a = [201701,'201702','201703','201704']
# b = [1000, 2000, 1500, 2100]
# plt.plot(a, b, 'b.-', label='line 4')
# plt.axis('auto')
# plt.legend()
# 
# plt.show()

plt.show()