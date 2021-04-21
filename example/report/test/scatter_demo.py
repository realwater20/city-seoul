"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax3 = fig.add_subplot(133)
ax4 = fig.add_subplot(211)
ax3 = fig.add_subplot(212)
ax4 = fig.add_subplot(213)
ax1.title.set_text('First Plot')
ax2.title.set_text('Second Plot')
ax3.title.set_text('Third Plot')
ax4.title.set_text('Fourth Plot')
plt.show()