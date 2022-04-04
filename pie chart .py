# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:13:16 2020

@author: Aditya
"""

import matplotlib.pyplot as pl
a=[22.2,17.6,8.8,8,7.7,6.7]
b=['JAVA','Python','PHP','JavaScript','C#','C++']
e=[0.2,0,0,0,0,0]
pl.pie(a,labels=b,explode=e,autopct="%3d%%")
pl.show()