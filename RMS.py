# -*- coding: utf-8 -*-

import raybundle as rp
import numpy as np

#%%
'''
Calculating the RMS of the ray positions from the optical axis at the paraxial focus.

Parameters
----------
rms_x : float
        the sum of all x positions squared
rms_y : float
        the sum of all y positions squared
RMS_x : list
        all x coordiates at the paraxial focus
'''

RMS_x = []
RMS_y = []

for l in rp.bundle1_focus:
    bundle_x = l[0]
    bundle_y = l[1]
    RMS_x.append(bundle_x)
    RMS_y.append(bundle_y)

for i in RMS_x:
    rms_x = sum([i**2])

for j in RMS_y:
    rms_y = sum([j**2])


def RMS(rms_x, rms_y, RMS_x):
    RMS = np.sqrt((rms_x + rms_y) / len(RMS_x))
    return RMS
print('the rootmean square of spot radius is', RMS(rms_x, rms_y, RMS_x), 'mm')
 

