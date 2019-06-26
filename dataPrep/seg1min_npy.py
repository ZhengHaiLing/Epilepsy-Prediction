# -*- coding: utf-8 -*-
"""seg1min_npy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1na5im_Q5KxTKGGhSbx9i28u1OFTPFdkh
"""

import tensorflow as tf
import scipy.io as sio
import os
import numpy as np

drivepath = '/content/drive/My Drive'
if os.path.isdir(drivepath) == False: # check google drive is mounted or not
  from google.colab import drive
  drive.mount('/content/drive')

###### interictal type #####
subname = 'Dog_1'
epitype = 'interictal'
n_inter = 480


for i in range(1, n_inter+1):
  filei = '{:0>4}'.format(i)

  pubdatasetpath = os.path.join(drivepath, 'Projects','Epilepsy', 'Prediction', 'KaggleComp')
  filename = subname + '_' + epitype + '_segment_' + filei + '.mat'
  matfile = os.path.join(pubdatasetpath,'OriginalData',subname,filename)
  
  print("dealing with " + str(i) + ":" + filename)

  # load .mat file
  matdata = sio.loadmat(matfile) 
  keys = list(matdata)

  # get the segment data
  for key in keys:
    if(key.find('_segment_')!=-1):
      segmentdata = matdata[key]
      break

  eeg10min = segmentdata[0][0][0]
  interval = 60 # segment to 1 min (60 s)
  fs = 400
  ntemporal = np.round_(interval * fs)

  # segment into 1 min eeg
  for segi in range(9):
    segdata = np.expand_dims(eeg10min[:,0:ntemporal], axis = 2)
    if segi == 0:
      eeg1min = segdata
    else:
      eeg1min = np.append(eeg1min, segdata, axis = 2)

  segdata = np.expand_dims(eeg10min[:, -ntemporal-1:-1], axis = 2) # the last segment
  eeg1min = np.append(eeg1min, segdata, axis = 2)

  # save part
  savefolder = os.path.join(pubdatasetpath, 'ProcessedData', 'Seg1min', subname)

  if os.path.isdir(savefolder) == False:
    print("make dir" + savefolder)
    os.mkdir(savefolder)
  savefilename = subname + '_' + epitype + '_seg1min_' + filei + '.npy'
  savefile = os.path.join(savefolder, savefilename)
  np.save(savefile, eeg1min)

##### preictal type #####
subname = 'Dog_1'
epitype = 'preictal'
n_pre = 24

for i in range(1, n_pre+1):
  filei = '{:0>4}'.format(i)

  pubdatasetpath = os.path.join(drivepath, 'Projects','Epilepsy', 'Prediction', 'KaggleComp')
  filename = subname + '_' + epitype + '_segment_' + filei + '.mat'
  matfile = os.path.join(pubdatasetpath,'OriginalData',subname,filename)
  
  print("dealing with " + str(i) + ":" + filename)

  # load .mat file
  matdata = sio.loadmat(matfile) 
  keys = list(matdata)

  # get the segment data
  for key in keys:
    if(key.find('_segment_')!=-1):
      segmentdata = matdata[key]
      break

  eeg10min = segmentdata[0][0][0]
  interval = 60 # segment to 1 min (60 s)
  fs = 400
  ntemporal = np.round_(interval * fs)

  # segment into 1 min eeg
  for segi in range(9):
    segdata = np.expand_dims(eeg10min[:,0:ntemporal], axis = 2)
    if segi == 0:
      eeg1min = segdata
    else:
      eeg1min = np.append(eeg1min, segdata, axis = 2)

  segdata = np.expand_dims(eeg10min[:, -ntemporal-1:-1], axis = 2) # the last segment
  eeg1min = np.append(eeg1min, segdata, axis = 2)

  # save part
  savefolder = os.path.join(pubdatasetpath, 'ProcessedData', 'Seg1min', subname)

  if os.path.isdir(savefolder) == False:
    print("make dir" + savefolder)
    os.mkdir(savefolder)
  savefilename = subname + '_' + epitype + '_seg1min_' + filei + '.npy'
  savefile = os.path.join(savefolder, savefilename)
  np.save(savefile, eeg1min)



