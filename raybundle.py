# -*- coding: utf-8 -*-

import numpy as np 
import math
from raytracer import SphericalRefraction
from raytracer import Ray
from raytracer import OutputPlane
import matplotlib.pyplot as plt

#%%
class RayBundle:
    '''
    RayBundle class represents a 3-d bundle of optical light ray, the rays are arranged in
    concentric circles in the x-y plane, centred at a centre ray with starting postion
    [0, 0, 0].
    '''
    def __init__(self, rays_per_ring, initial_direction, radii):
        '''
        Contains all necessary attributes for the class.
        
        Parameters
        ----------
        rays_per_ring      : list
                             the number of rays per concentric ring
        initial_direction  : list
                             starting direction vector of the ray bundle
        radii              : float
                             radius of each concentric ring

        '''
        
        self._ring_n = rays_per_ring
        
        self._initial_k = initial_direction
        
        self._ring_r = radii
        
        self._bundles = []
        
        self._spots = []
    
        #gap between each ring
        gap = np.linspace(0, radii, len(rays_per_ring)+1)
        
        #there are multiple rays per ring, so need to use enumerate
        for n, rays_per_ring in enumerate(rays_per_ring):
            for theta in np.linspace(0, 2 * math.pi, rays_per_ring+1):
                x = gap[n] * np.cos(theta)
                y = gap[n] * np.sin(theta)
                spots = [x, y, 0]
                bundle_rays = Ray([x, y, 0], self._initial_k)
                self._bundles.append(bundle_rays)
                self._spots.append(spots)
                
    def bundle(self):
        '''
        List of all the rays in a bundle.
        '''
        return self._bundles
    
    def bundle_spot(self):
        '''
        List of starting positions of the rays in the concentric rings.
        '''
        return self._spots
    
    def plot0(self, ax, color):
        '''
        Plots the z and x vertices of the ray.
        '''
        ax.plot((self.bundle()[0]).vertices()[2], (self.bundle()[0]).vertices()[0], color = color)
    

#%%
'''
Define objects representing SphericalRefraction, OutputPlane, RayBundle and the rays,
and input appropriate parameter values.

'''
sphere0= SphericalRefraction(100, 0.03, 1, 1.5, 100)

plane0 = OutputPlane(200)

bundle0 = RayBundle([1, 6, 12, 18, 24, 30], [0, 0, 100], 3)   
bundle1 = bundle0.bundle()

bundle01 = RayBundle([1, 6, 12, 18, 24, 30], [5, 0, 100], 3)   
bundle2 = bundle01.bundle()
#%%
'''
Plot the ray bundles
'''
fig,ax = plt.subplots()

bundle1_focus = [] #list of ray positions on the output plane (the focus) for bundle1
bundle2_focus = [] #list of ray positions on the output plane (the focus) for bundle2

for u in range(len(bundle1)):
    sphere0.propagate_ray(bundle1[u])
    plane0.propagate_ray(bundle1[u])
    bundle1[u].plot0(ax, color = 'royalblue')
    bundle1_focus.append(bundle1[u].p())


for v in range(len(bundle2)):
    sphere0.propagate_ray(bundle2[v])
    plane0.propagate_ray(bundle2[v])
    bundle2[v].plot0(ax, color = 'palevioletred')
    bundle2_focus.append(bundle2[v].p())

sphere0.plot0(ax)
plane0.plot0()

plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('ray bundles in x-z plane')
plt.ylim(-10, 10)
plt.legend(['bundle1','bundle2'])
ax = plt.gca()
leg = ax.get_legend()
leg.legendHandles[0].set_color('royalblue')
leg.legendHandles[1].set_color('palevioletred')
plt.show()
 
#%%
'''
Plot the spot diagram for bundle1 at z=0
'''
for p in bundle0.bundle_spot():
    bundle_x = p[0]
    bundle_y = p[1]
    plt.scatter(bundle_x, bundle_y, c ='royalblue')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.title('spot diagram of bundle1 at z=0')
plt.show()

#%%
'''
Plot the spot diagram for bundle2 at z=0
'''
for q in bundle01.bundle_spot():
    bundle_x = q[0]
    bundle_y = q[1]
    plt.scatter(bundle_x, bundle_y, c ='palevioletred')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.title('spot diagram of bundle2 at z=0')
plt.show()
#%%
'''
Plot the spot diagram for bundle1 at the focus
'''
for m in bundle1_focus:
    bundle_x = m[0]
    bundle_y = m[1]
    plt.scatter(bundle_x, bundle_y, c = 'royalblue')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.title('spot diagram of bundle1 at the focus')
plt.show()
#%%
'''
Plot the spot diagram for bundle2 at the focus
'''
for n in bundle2_focus:
    bundle_x = n[0]
    bundle_y = n[1]
    plt.scatter(bundle_x, bundle_y, c = 'palevioletred')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.title('spot diagram of bundle2 at the focus')
plt.show()
#%%
