# -*- coding: utf-8 -*-


from raytracer import SphericalRefraction
from raytracer import Ray
from raytracer import OutputPlane
import raybundle as rp
from single_spherical_refracting_surface import ParaxialFocus
import matplotlib.pyplot as plt
import numpy as np
#%%
'''
Plano-convex
'''
plano = SphericalRefraction(160, 1e-100, 1, 1.5168, 100)
convex = SphericalRefraction(165, -0.02, 1, 1.5168, 100)
plane2 = OutputPlane(270)

ray0 = Ray([0,0,0],[0,0,100]) #the optial axis
ray1 = Ray([3,0,0],[0,0,150])
ray2 = Ray([5,0,0],[0,0,200])
ray3 = Ray([7,0,0],[0,0,100])
ray4 = Ray([-3,0,0],[0,0,150])
ray5 = Ray([-5,0,0],[0,0,200])
ray6 = Ray([-7,0,0],[0,0,200])
ray7 = Ray([0.1,0,0],[0,0,200])

plano.propagate_ray(ray0)
convex.propagate_ray(ray0)
plane2.propagate_ray(ray0)
plano.propagate_ray(ray1)
convex.propagate_ray(ray1)
plane2.propagate_ray(ray1)
plano.propagate_ray(ray2)
convex.propagate_ray(ray2)
plane2.propagate_ray(ray2)
plano.propagate_ray(ray3)
convex.propagate_ray(ray3)
plane2.propagate_ray(ray3)
plano.propagate_ray(ray4)
convex.propagate_ray(ray4)
plane2.propagate_ray(ray4)
plano.propagate_ray(ray5)
convex.propagate_ray(ray5)
plane2.propagate_ray(ray5)
plano.propagate_ray(ray6)
convex.propagate_ray(ray6)
plane2.propagate_ray(ray6)
plano.propagate_ray(ray7)
convex.propagate_ray(ray7)
plane2.propagate_ray(ray7)

fig,ax = plt.subplots()
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('plano-convex singlet lens')
ray0.plot0(ax, color = 'blue')
ray1.plot0(ax, color = 'orange')
ray2.plot0(ax, color = 'plum')
ray3.plot0(ax, color = 'green')
ray4.plot0(ax, color = 'red')
ray5.plot0(ax, color = 'brown')
ray6.plot0(ax, color = 'pink')
ray7.plot0(ax, color = 'olive')
plane2.plot0()

#----------

print('The paraxial focus of PC lens is', ParaxialFocus(0.10, 65, ray7.p()[0], ray7.p()[2], 0, 50, 0, 250))

#%%
'''
Ray bundle for plano-convex
'''
bundle02 = rp.RayBundle([1, 6, 12, 18, 24, 30], [0, 0, 100], 6)   
bundle3 = bundle02.bundle()

fig,ax = plt.subplots()

bundle3_focus = []


for u in range(len(bundle3)):
    plano.propagate_ray(bundle3[u])
    convex.propagate_ray(bundle3[u])
    plane2.propagate_ray(bundle3[u])
    bundle3[u].plot0(ax, color = 'royalblue')
    bundle3_focus.append(bundle3[u].p())

plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('ray bundle refracted by plano-convex lens')
plane2.plot0()
plt.show()
#%%
'''
Convex-plano
'''
convex1 = SphericalRefraction(160, 0.02, 1, 1.5168, 100)
plano1 = SphericalRefraction(165, 1e-100, 1.5168, 1, 100)
plane2 = OutputPlane(270)

ray0 = Ray([0,0,0],[0,0,100]) #the optial axis
ray1 = Ray([3,0,0],[0,0,150])
ray2 = Ray([5,0,0],[0,0,200])
ray3 = Ray([7,0,0],[0,0,100])
ray4 = Ray([-3,0,0],[0,0,150])
ray5 = Ray([-5,0,0],[0,0,200])
ray6 = Ray([-7,0,0],[0,0,200])
ray7 = Ray([0.1,0,0],[0,0,200])


convex1.propagate_ray(ray0)
plano1.propagate_ray(ray0)
plane2.propagate_ray(ray0)
convex1.propagate_ray(ray1)
plano1.propagate_ray(ray1)
plane2.propagate_ray(ray1)
convex1.propagate_ray(ray2)
plano1.propagate_ray(ray2)
plane2.propagate_ray(ray2)
convex1.propagate_ray(ray3)
plano1.propagate_ray(ray3)
plane2.propagate_ray(ray3)
convex1.propagate_ray(ray4)
plano1.propagate_ray(ray4)
plane2.propagate_ray(ray4)
convex1.propagate_ray(ray5)
plano1.propagate_ray(ray5)
plane2.propagate_ray(ray5)
convex1.propagate_ray(ray6)
plano1.propagate_ray(ray6)
plane2.propagate_ray(ray6)
convex1.propagate_ray(ray7)
plano1.propagate_ray(ray7)
plane2.propagate_ray(ray7)

fig,ax = plt.subplots()
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('convex-plano singlet lens')
ray0.plot0(ax, color = 'blue')
ray1.plot0(ax, color = 'orange')
ray2.plot0(ax, color = 'plum')
ray3.plot0(ax, color = 'green')
ray4.plot0(ax, color = 'red')
ray5.plot0(ax, color = 'brown')
ray6.plot0(ax, color = 'pink')
ray7.plot0(ax, color = 'olive')
plane2.plot0()

#----------

print('The paraxial focus of CP lens is', ParaxialFocus(0.10, 160, ray7.p()[0], ray7.p()[2], 0, 50, 0, 250))

#%%
'''
Ray bundle for convex-plano
'''
bundle02 = rp.RayBundle([1, 6, 12, 18, 24, 30], [0, 0, 100], 6)   
bundle4 = bundle02.bundle()

fig,ax = plt.subplots()

bundle4_focus = []


for u in range(len(bundle4)):
    convex1.propagate_ray(bundle4[u])
    plano1.propagate_ray(bundle4[u])
    plane2.propagate_ray(bundle4[u])
    bundle4[u].plot0(ax, color = 'palevioletred')
    bundle4_focus.append(bundle4[u].p())

plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('ray bundles refracted by convex-plano lens')
plane2.plot0()
plt.show()

#----------

RMS_x = []
RMS_y = []

for l in bundle4_focus:
    bundle_x = l[0]
    bundle_y = l[1]
    RMS_x.append(bundle_x)
    RMS_y.append(bundle_y)

for i in RMS_x:
    rms_x = sum([i**2])

for j in RMS_y:
    rms_y = sum([j**2])

RMS = np.sqrt((rms_x + rms_y) / len(RMS_x))
print('the rootmean square of spot radius of CP lens is', RMS, 'mm')


