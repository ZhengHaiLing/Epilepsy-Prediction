# -*- coding: utf-8 -*-
"""loadseg1min_npy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VA_JNCwUY66JcGVLJdtvJukFqRlb_h04
"""

drivepath = '/content/drive/My Drive'
if os.path.isdir(drivepath) == False: # check google drive is mounted or not
  from google.colab import drive
  drive.mount('/content/drive')

import scipy.io as sio
import os
import numpy as np

subname = 'Dog_1'
epitype = 'interictal'
i = 1
filei = '{:0>4}'.format(i)

pubdatasetpath = os.path.join(drivepath, 'Projects','Epilepsy', 'Prediction', 'KaggleComp')
filefolder = os.path.join(pubdatasetpath, 'ProcessedData', 'Seg1min', subname)
filename = subname + '_' + epitype + '_seg1min_' + filei + '.npy'
loadfile = os.path.join(filefolder, filename)

seg1min = np.load(loadfile)

print(seg1min.shape)

