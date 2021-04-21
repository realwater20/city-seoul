# -*- coding: utf-8 -*- 
# 다른축을 참조하는 plot 겹쳐서 표현하기
import numpy as np
import matplotlib.pyplot as plt

t = [1.,2.,3.,4.]
aa=[11.4, 12.7, 13.1, 14.56]
plt.plot(t, aa, 'b-o', label="aa")
plt.text(3,14.7,"<--------------- aa",verticalalignment='top', 
horizontalalignment='right') 
plt.xlabel('no')
plt.ylabel('aa')

cc=[10.4, 10.7, 9.1, 13.56]
plt.plot(t, cc, 'g-o', label="cc")
plt.text(3,14.7,"<--------------- cc",verticalalignment='top', 
horizontalalignment='right') 
plt.xlabel('no')
plt.ylabel('aa')

ax2 = plt.twinx()
bb = [0.9, 2.2, 3.54, 4.0]
plt.plot(t, bb, 'r-s',label="bb")
plt.text(3,2.2,"bb ------------------>",verticalalignment='top', 
horizontalalignment='left') 
plt.ylabel('bb')
ax2.yaxis.tick_right()
plt.show()


