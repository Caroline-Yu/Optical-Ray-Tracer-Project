# -*- coding: utf-8 -*-

import numpy as np 
from raytracer import SphericalRefraction
from raytracer import Ray
from raytracer import OutputPlane
import matplotlib.pyplot as plt
#%%
#test for my raise exception code
print('hello')
R1 = Ray(p = [1, 2, 3], k = [1, 2, 3])

#test for the append method
R2 = Ray(p = [1, 3, 5], k = [3, 4, 5])


#%%Task 5, using the vectior form te Snell's law to determine the direction of the refracted ray, k2_hat
#Derivation from Stack Exchange: https://physics.stackexchange.com/questions/435512/snells-law-in-vector-form and my lab book

def refraction(n_hat, k1_hat, n1, n2):
    return (np.sqrt(1 - ((n1/n2)**2) * ((1 - np.dot(n_hat, k1_hat))**2)) * (n_hat)) + ((n1/n2) * (k1_hat - ((np.dot(n_hat, k1_hat)) * n_hat)))

#%%
#Task 5, using the vectior form te Snell's law to determine the direction
#of the refracted ray, k2_hat
#Derivation from StarkEffects.com
#http://www.starkeffects.com/snells-law-vector.shtml
#N is the normalised normal vector
#k1_hat is the normalised incident light vector
#n1 and n2 are the refractive indices'''

def refraction2(N, k1_hat, n1, n2):
    return (n1/n2) * (np.cross(N, np.cross(-N, k1_hat))) - (N * np.sqrt(1 - (n1/n2)**2 * (np.dot(np.cross(N, k1_hat), np.cross(N, k1_hat)))))

#%%
#To test the function refraction, using the example from StarkEffects.com
#http://www.starkeffects.com/snells-law-vector.shtml
#The correct answer of k2_hat is np.array([0.471, 0, 0.882])'''

n_hat_test = np.array([0, 0, -1])
k1_hat_test = np.array([0.707, 0, 0.707])
n1_test = 1
n2_test = 1.5

print ('The k2_hat vector is', refraction(n_hat_test, k1_hat_test, n1_test, n2_test))

#%%The console returns: RuntimeWarning: invalid value encountered in sqrt, to save time I just decided to just use 
#a complete different function'''
#To test the function refraction2, using the example from StarkEffects.com
#http://www.starkeffects.com/snells-law-vector.shtml
#The correct answer of k2_hat is np.array([0.471, 0, 0.882])'''

print ('The k2_hat vector is', refraction2(n_hat_test, k1_hat_test, n1_test, n2_test))

#The console returns: The k2_hat vector is [ 0.47133333 -0.          0.88195515] which is the correct answer
#%%
'''
Test for task 13
'''
plane = OutputPlane(i_out = 10) #define the OutputPlane class as an object
ray = Ray(p = [0,0,0], k=[0,1,1]) #make a ray 
plane.propagate_ray(ray) #using the propagate_ray method in the OutputPlane class
print(ray.p()) #should print [0, 10, 10]; and it does
plt.figure()
plt.title('z = 10')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(plane.x, plane.y)
#This is test is successfuly because the plot has one point with x-y coordinate (0, 10)
#%%
'''
Test for task 13
'''
from raybundle_plot import RayBundle
sphere0= SphericalRefraction(100, 0.03, 1, 1.5, 100)

plane0 = OutputPlane(200)

bundle0 = RayBundle([1, 6, 12, 18, 24, 30], [0, 0, 1], [0, 0, 0], 2.5)   
bundle1 = bundle0.bundle()
bundle1_ray = bundle1[0]
plt.scatter(bundle1[0].vertices()[0], bundle1[0].vertices()[1])
plt.show()  
         