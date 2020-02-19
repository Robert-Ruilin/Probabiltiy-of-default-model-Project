# -*- coding: utf-8 -*-
"""
Time series analysis - PD 5 days reaction

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline

PD_Moody_5 = pd.read_excel("PD 5 day.xlsx", index_col = 0, columns = 0)
PD_Moody_5.iloc[:6,:] = PD_Moody_5.iloc[:6,:]*10000

'''PD fluctuation during 5 days pre-creidt rating upgrading'''
fig, ((ax1, ax2, ax3, ax4, ax5),
      (ax6, ax7, ax8, ax9, ax10),
      (ax11, ax12, ax13, ax14, ax15),
      (ax16, ax17, ax18, ax19, ax20),
      (ax21, ax22, ax23, ax24, ax25)) = plt.subplots(5,5,figsize=[20,18])
    
x = np.array([-5,-4,-3,-2,-1,0],dtype='float64')
xnew = np.linspace(x.min(),x.max(),300)

y1 = np.array(PD_Moody_5.iloc[:6,0],dtype='float64')
y_smooth1 = spline(x,y1,xnew)
#ax1.plot(x,y1)
ax1.plot(xnew,y_smooth1, color='red')
ax1.set_xlim(-5,0,1)
ax1.set_xlabel('1 notch')
ax1.set_ylabel("CRI 1 yr PD (bps)")

y2 = np.array(PD_Moody_5.iloc[:6,3],dtype='float64')
y_smooth2 = spline(x,y2,xnew)
#ax2.plot(x,y2)
ax2.plot(xnew,y_smooth2, color='red')
ax2.set_xlim(-5,0,1)
ax2.set_xlabel('1 notch')

y3 = np.array(PD_Moody_5.iloc[:6,4],dtype='float64')
y_smooth3 = spline(x,y3,xnew)
#ax3.plot(x,y3)
ax3.plot(xnew,y_smooth3, color='red')
ax3.set_xlim(-5,0,1)
ax3.set_xlabel('1 notch')

y4 = np.array(PD_Moody_5.iloc[:6,7],dtype='float64')
y_smooth4 = spline(x,y4,xnew)
#ax4.plot(x,y4)
ax4.plot(xnew,y_smooth4, color='red')
ax4.set_xlim(-5,0,1)
ax4.set_xlabel('1 notch')

y5 = np.array(PD_Moody_5.iloc[:6,8],dtype='float64')
y_smooth5 = spline(x,y5,xnew)
#ax5.plot(x,y5)
ax5.plot(xnew,y_smooth5, color='red')
ax5.set_xlim(-5,0,1)
ax5.set_xlabel('1 notch')

y6 = np.array(PD_Moody_5.iloc[:6,12],dtype='float64')
y_smooth6 = spline(x,y6,xnew)
#ax6.plot(x,y6)
ax6.plot(xnew,y_smooth6, color='red')
ax6.set_xlim(-5,0,1)
ax6.set_xlabel('1 notch')
ax6.set_ylabel("CRI 1 yr PD (bps)")

y7 = np.array(PD_Moody_5.iloc[:6,14],dtype='float64')
y_smooth7 = spline(x,y7,xnew)
#ax7.plot(x,y7)
ax7.plot(xnew,y_smooth7, color='red')
ax7.set_xlim(-5,0,1)
ax7.set_xlabel('1 notch')

y8 = np.array(PD_Moody_5.iloc[:6,15],dtype='float64')
y_smooth8 = spline(x,y8,xnew)
#ax8.plot(x,y8)
ax8.plot(xnew,y_smooth8, color='red')
ax8.set_xlim(-5,0,1)
ax8.set_xlabel('1 notch')

y9 = np.array(PD_Moody_5.iloc[:6,18],dtype='float64')
y_smooth9 = spline(x,y9,xnew)
#ax9.plot(x,y9)
ax9.plot(xnew,y_smooth9, color='red')
ax9.set_xlim(-5,0,1)
ax9.set_xlabel('1 notch')

y10 = np.array(PD_Moody_5.iloc[:6,20],dtype='float64')
y_smooth10 = spline(x,y10,xnew)
#ax10.plot(x,y10)
ax10.plot(xnew,y_smooth10, color='red')
ax10.set_xlim(-5,0,1)
ax10.set_xlabel('1 notch')

y11 = np.array(PD_Moody_5.iloc[:6,24],dtype='float64')
y_smooth11 = spline(x,y11,xnew)
#ax11.plot(x,y11)
ax11.plot(xnew,y_smooth11, color='red')
ax11.set_xlim(-5,0,1)
ax11.set_xlabel('1 notch')
ax11.set_ylabel("CRI 1 yr PD (bps)")

y12 = np.array(PD_Moody_5.iloc[:6,26],dtype='float64')
y_smooth12 = spline(x,y12,xnew)
#ax12.plot(x,y12)
ax12.plot(xnew,y_smooth12, color='red')
ax12.set_xlim(-5,0,1)
ax12.set_xlabel('1 notch')

y13 = np.array(PD_Moody_5.iloc[:6,28],dtype='float64')
y_smooth13 = spline(x,y13,xnew)
#ax13.plot(x,y13)
ax13.plot(xnew,y_smooth13, color='red')
ax13.set_xlim(-5,0,1)
ax13.set_xlabel('1 notch')

y14 = np.array(PD_Moody_5.iloc[:6,31],dtype='float64')
y_smooth14 = spline(x,y14,xnew)
#ax14.plot(x,y14)
ax14.plot(xnew,y_smooth14, color='red')
ax14.set_xlim(-5,0,1)
ax14.set_xlabel('1 notch')

y15 = np.array(PD_Moody_5.iloc[:6,32],dtype='float64')
y_smooth15 = spline(x,y15,xnew)
#ax15.plot(x,y15)
ax15.plot(xnew,y_smooth15, color='red')
ax15.set_xlim(-5,0,1)
ax15.set_xlabel('1 notch')

y16 = np.array(PD_Moody_5.iloc[:6,36],dtype='float64')
y_smooth16 = spline(x,y16,xnew)
#ax16.plot(x,y16)
ax16.plot(xnew,y_smooth16, color='red')
ax16.set_xlim(-5,0,1)
ax16.set_xlabel('1 notch')
ax16.set_ylabel("CRI 1 yr PD (bps)")

y17 = np.array(PD_Moody_5.iloc[:6,38],dtype='float64')
y_smooth17 = spline(x,y17,xnew)
#ax17.plot(x,y17)
ax17.plot(xnew,y_smooth17, color='red')
ax17.set_xlim(-5,0,1)
ax17.set_xlabel('1 notch')

y18 = np.array(PD_Moody_5.iloc[:6,39],dtype='float64')
y_smooth18 = spline(x,y18,xnew)
#ax18.plot(x,y18)
ax18.plot(xnew,y_smooth18, color='red')
ax18.set_xlim(-5,0,1)
ax18.set_xlabel('1 notch')

y19 = np.array(PD_Moody_5.iloc[:6,41],dtype='float64')
y_smooth19 = spline(x,y19,xnew)
#ax19.plot(x,y19)
ax19.plot(xnew,y_smooth19, color='red')
ax19.set_xlim(-5,0,1)
ax19.set_xlabel('1 notch')

y20 = np.array(PD_Moody_5.iloc[:6,42],dtype='float64')
y_smooth20 = spline(x,y20,xnew)
#ax20.plot(x,y20)
ax20.plot(xnew,y_smooth20, color='red')
ax20.set_xlim(-5,0,1)
ax20.set_xlabel('1 notch')

y21 = np.array(PD_Moody_5.iloc[:6,43],dtype='float64')
y_smooth21 = spline(x,y21,xnew)
#ax21.plot(x,y21)
ax21.plot(xnew,y_smooth21, color='red')
ax21.set_xlim(-5,0,1)
ax21.set_xlabel('1 notch')
ax21.set_ylabel("CRI 1 yr PD (bps)")

y22 = np.array(PD_Moody_5.iloc[:6,44],dtype='float64')
y_smooth22 = spline(x,y22,xnew)
#ax22.plot(x,y22)
ax22.plot(xnew,y_smooth22, color='red')
ax22.set_xlim(-5,0,1)
ax22.set_xlabel('1 notch')

fig.delaxes(ax23)
fig.delaxes(ax24)
fig.delaxes(ax25)

plt.show()

'''PD fluctuation during 20 days pre-creidt rating downgrading'''
fig, ((ax1, ax2, ax3, ax4, ax5),
      (ax6, ax7, ax8, ax9, ax10),
      (ax11, ax12, ax13, ax14, ax15),
      (ax16, ax17, ax18, ax19, ax20),
      (ax21, ax22, ax23, ax24, ax25)) = plt.subplots(5,5,figsize=[20,18])
    
x = np.array([-5,-4,-3,-2,-1,0],dtype='float64')
xnew = np.linspace(x.min(),x.max(),300)

y1 = np.array(PD_Moody_5.iloc[:6,1],dtype='float64')
y_smooth1 = spline(x,y1,xnew)
#ax1.plot(x,y1)
ax1.plot(xnew,y_smooth1, color='red')
ax1.set_xlim(-5,0,1)
ax1.set_xlabel('2 notches')
ax1.set_ylabel("CRI 1 yr PD (bps)")

y2 = np.array(PD_Moody_5.iloc[:6,2],dtype='float64')
y_smooth2 = spline(x,y2,xnew)
#ax2.plot(x,y2)
ax2.plot(xnew,y_smooth2, color='red')
ax2.set_xlim(-5,0,1)
ax2.set_xlabel('2 notches')

y3 = np.array(PD_Moody_5.iloc[:6,5],dtype='float64')
y_smooth3 = spline(x,y3,xnew)
#ax3.plot(x,y3)
ax3.plot(xnew,y_smooth3, color='red')
ax3.set_xlim(-5,0,1)
ax3.set_xlabel('1 notch')

y4 = np.array(PD_Moody_5.iloc[:6,6],dtype='float64')
y_smooth4 = spline(x,y4,xnew)
#ax4.plot(x,y4)
ax4.plot(xnew,y_smooth4, color='red')
ax4.set_xlim(-5,0,1)
ax4.set_xlabel('1 notch')

y5 = np.array(PD_Moody_5.iloc[:6,9],dtype='float64')
y_smooth5 = spline(x,y5,xnew)
#ax5.plot(x,y5)
ax5.plot(xnew,y_smooth5, color='red')
ax5.set_xlim(-5,0,1)
ax5.set_xlabel('1 notch')

y6 = np.array(PD_Moody_5.iloc[:6,10],dtype='float64')
y_smooth6 = spline(x,y6,xnew)
#ax6.plot(x,y6)
ax6.plot(xnew,y_smooth6, color='red')
ax6.set_xlim(-5,0,1)
ax6.set_xlabel('1 notch')
ax6.set_ylabel("CRI 1 yr PD (bps)")

y7 = np.array(PD_Moody_5.iloc[:6,11],dtype='float64')
y_smooth7 = spline(x,y7,xnew)
#ax7.plot(x,y7)
ax7.plot(xnew,y_smooth7, color='red')
ax7.set_xlim(-5,0,1)
ax7.set_xlabel('1 notch')

y8 = np.array(PD_Moody_5.iloc[:6,13],dtype='float64')
y_smooth8 = spline(x,y8,xnew)
#ax8.plot(x,y8)
ax8.plot(xnew,y_smooth8, color='red')
ax8.set_xlim(-5,0,1)
ax8.set_xlabel('1 notch')

y9 = np.array(PD_Moody_5.iloc[:6,16],dtype='float64')
y_smooth9 = spline(x,y9,xnew)
#ax9.plot(x,y9)
ax9.plot(xnew,y_smooth9, color='red')
ax9.set_xlim(-5,0,1)
ax9.set_xlabel('3 notches')

y10 = np.array(PD_Moody_5.iloc[:6,17],dtype='float64')
y_smooth10 = spline(x,y10,xnew)
#ax10.plot(x,y10)
ax10.plot(xnew,y_smooth10, color='red')
ax10.set_xlim(-5,0,1)
ax10.set_xlabel('1 notch')

y11 = np.array(PD_Moody_5.iloc[:6,19],dtype='float64')
y_smooth11 = spline(x,y11,xnew)
#ax11.plot(x,y11)
ax11.plot(xnew,y_smooth11, color='red')
ax11.set_xlim(-5,0,1)
ax11.set_xlabel('3 notches')
ax11.set_ylabel("CRI 1 yr PD (bps)")

y12 = np.array(PD_Moody_5.iloc[:6,21],dtype='float64')
y_smooth12 = spline(x,y12,xnew)
#ax12.plot(x,y12)
ax12.plot(xnew,y_smooth12, color='red')
ax12.set_xlim(-5,0,1)
ax12.set_xlabel('6 notches')

y13 = np.array(PD_Moody_5.iloc[:6,22],dtype='float64')
y_smooth13 = spline(x,y13,xnew)
#ax13.plot(x,y13)
ax13.plot(xnew,y_smooth13, color='red')
ax13.set_xlim(-5,0,1)
ax13.set_xlabel('1 notch')

y14 = np.array(PD_Moody_5.iloc[:6,23],dtype='float64')
y_smooth14 = spline(x,y14,xnew)
#ax14.plot(x,y14)
ax14.plot(xnew,y_smooth14, color='red')
ax14.set_xlim(-5,0,1)
ax14.set_xlabel('1 notch')

y15 = np.array(PD_Moody_5.iloc[:6,25],dtype='float64')
y_smooth15 = spline(x,y15,xnew)
#ax15.plot(x,y15)
ax15.plot(xnew,y_smooth15, color='red')
ax15.set_xlim(-5,0,1)
ax15.set_xlabel('2 notch')

y16 = np.array(PD_Moody_5.iloc[:6,27],dtype='float64')
y_smooth16 = spline(x,y16,xnew)
#ax16.plot(x,y16)
ax16.plot(xnew,y_smooth16, color='red')
ax16.set_xlim(-5,0,1)
ax16.set_xlabel('1 notch')
ax16.set_ylabel("CRI 1 yr PD (bps)")

y17 = np.array(PD_Moody_5.iloc[:6,29],dtype='float64')
y_smooth17 = spline(x,y17,xnew)
#ax17.plot(x,y17)
ax17.plot(xnew,y_smooth17, color='red')
ax17.set_xlim(-5,0,1)
ax17.set_xlabel('1 notch')

y18 = np.array(PD_Moody_5.iloc[:6,30],dtype='float64')
y_smooth18 = spline(x,y18,xnew)
#ax18.plot(x,y18)
ax18.plot(xnew,y_smooth18, color='red')
ax18.set_xlim(-5,0,1)
ax18.set_xlabel('1 notch')

y19 = np.array(PD_Moody_5.iloc[:6,33],dtype='float64')
y_smooth19 = spline(x,y19,xnew)
#ax19.plot(x,y19)
ax19.plot(xnew,y_smooth19, color='red')
ax19.set_xlim(-5,0,1)
ax19.set_xlabel('1 notch')

y20 = np.array(PD_Moody_5.iloc[:6,34],dtype='float64')
y_smooth20 = spline(x,y20,xnew)
#ax20.plot(x,y20)
ax20.plot(xnew,y_smooth20, color='red')
ax20.set_xlim(-5,0,1)
ax20.set_xlabel('1 notch')

y21 = np.array(PD_Moody_5.iloc[:6,35],dtype='float64')
y_smooth21 = spline(x,y21,xnew)
#ax21.plot(x,y21)
ax21.plot(xnew,y_smooth21, color='red')
ax21.set_xlim(-5,0,1)
ax21.set_xlabel('1 notch')
ax21.set_ylabel("CRI 1 yr PD (bps)")

y22 = np.array(PD_Moody_5.iloc[:6,37],dtype='float64')
y_smooth22 = spline(x,y22,xnew)
#ax22.plot(x,y22)
ax22.plot(xnew,y_smooth22, color='red')
ax22.set_xlim(-5,0,1)
ax22.set_xlabel('1 notch')

y23 = np.array(PD_Moody_5.iloc[:6,40],dtype='float64')
y_smooth23 = spline(x,y23,xnew)
#ax23.plot(x,y23)
ax23.plot(xnew,y_smooth23, color='red')
ax23.set_xlim(-5,0,1)
ax23.set_xlabel('1 notch')

y24 = np.array(PD_Moody_5.iloc[:6,45],dtype='float64')
y_smooth24 = spline(x,y24,xnew)
#ax24.plot(x,y24)
ax24.plot(xnew,y_smooth24, color='red')
ax24.set_xlim(-5,0,1)
ax24.set_xlabel('1 notch')

fig.delaxes(ax25)

plt.show()

        
    

