# -*- coding: utf-8 -*-


from raytracer import SphericalRefraction
from raytracer import Ray
from raytracer import OutputPlane
import raybundle as rp
import matplotlib.pyplot as plt

#%%
'''
Testing my model with a single spherical refracting surface ad the output plane
I also added a plot0 method to each of my class
'''
#%%
'''
Here I defined all the spherical refeaction parameters as given in the task
I ctreated several collimated incident rays to test all the classes in the raytracer module
'''
sphere0 = SphericalRefraction(100, 0.03, 1, 1.5, 100)
plane0 = OutputPlane(250)

#individual rays
ray0 = Ray([0,0,0],[0,0,100]) #the optial axis
ray1 = Ray([3,0,0],[0,0,150])
ray2 = Ray([5,0,0],[0,0,200])
ray3 = Ray([7,0,0],[0,0,100])
ray4 = Ray([-3,0,0],[0,0,150])
ray5 = Ray([-5,0,0],[0,0,200])
ray6 = Ray([-7,0,0],[0,0,200])
ray7 = Ray([0.1,0,0],[0,0,200])

sphere0.propagate_ray(ray0)
plane0.propagate_ray(ray0)
sphere0.propagate_ray(ray1)
plane0.propagate_ray(ray1)
sphere0.propagate_ray(ray2)
plane0.propagate_ray(ray2)
sphere0.propagate_ray(ray3)
plane0.propagate_ray(ray3)
sphere0.propagate_ray(ray4)
plane0.propagate_ray(ray4)
sphere0.propagate_ray(ray5)
plane0.propagate_ray(ray5)
sphere0.propagate_ray(ray6)
plane0.propagate_ray(ray6)
sphere0.propagate_ray(ray7)
plane0.propagate_ray(ray7)

fig,ax = plt.subplots()
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('single spherical refracting surface(positive curvature)- collimated beams')
ray0.plot0(ax, color = 'blue')
ray1.plot0(ax, color = 'orange')
ray2.plot0(ax, color = 'plum')
ray3.plot0(ax, color = 'green')
ray4.plot0(ax, color = 'red')
ray5.plot0(ax, color = 'brown')
ray6.plot0(ax, color = 'pink')
ray7.plot0(ax, color = 'olive')
sphere0.plot0(ax)
plane0.plot0()


#%%
'''TASK 10
Estimate the position of the paraxial focus using paraxial rays
By finding the the intersection of two lines, L1 and L2
L1      the paraxial ray
L2      the optical axis
The two lines are defind by extracting two points from each line
L1      (x1, z1) and (x2, z2)
L2      (x3, z3) and (x4, z4)
'''

x1 = 0.10 #the x component of the paraxial ray
z1 = 100.00 #where the paraxial ray intersects the curvature
x2 = ray7.p()[0]
z2 = ray7.p()[2]

x3 = 0
z3 = 50
x4 = 0
z4 = 250

def ParaxialFocus(x1, z1, x2, z2, x3, z3, x4, z4):
    Pz = ((z1 * x2 - x1 * z2) * (z3 - z4) - (z1 - z2) * (z3 * x4 - x4 * z4)) / ((z1 - z2) * (x3 - x4) - (x1 - x2) * (z3 - z4))
    return Pz

print('The paraxial focus is', ParaxialFocus(0.10, 100, ray7.p()[0], ray7.p()[2], 0, 50, 0, 250))

#%%
'''
This cell tests my code for incident rays from different directions
'''
ray00 = Ray([0,0,0],[0,0,100]) #the optial axis
ray01 = Ray([0,0,0],[4,0,100])
ray02 = Ray([0,0,0],[3,0,100])
ray03 = Ray([0,0,0],[2,0,100])
ray04 = Ray([0,0,0],[1,0,100])
ray05 = Ray([0,0,0],[-1,0,100])
ray06 = Ray([0,0,0],[-2,0,100])
ray07 = Ray([0,0,0],[-3,0,100])
ray08 = Ray([0,0,0],[-4,0,100])

sphere0.propagate_ray(ray00)
plane0.propagate_ray(ray00)
sphere0.propagate_ray(ray01)
plane0.propagate_ray(ray01)
sphere0.propagate_ray(ray02)
plane0.propagate_ray(ray02)
sphere0.propagate_ray(ray03)
plane0.propagate_ray(ray03)
sphere0.propagate_ray(ray04)
plane0.propagate_ray(ray04)
sphere0.propagate_ray(ray05)
plane0.propagate_ray(ray05)
sphere0.propagate_ray(ray06)
plane0.propagate_ray(ray06)
sphere0.propagate_ray(ray07)
plane0.propagate_ray(ray07)
sphere0.propagate_ray(ray08)
plane0.propagate_ray(ray08)

fig,ax = plt.subplots()
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('single spherical refracting surface(positive curvature)')
ray00.plot0(ax, color = 'blue')
ray01.plot0(ax, color = 'orange')
ray02.plot0(ax, color = 'plum')
ray03.plot0(ax, color = 'green')
ray04.plot0(ax, color = 'red')
ray05.plot0(ax, color = 'brown')
ray06.plot0(ax, color = 'pink')
ray07.plot0(ax, color = 'olive')
ray08.plot0(ax, color = 'gold')
sphere0.plot0(ax)
plane0.plot0()

#%%
'''
This cell tests my code for negative curvature
'''
sphere1 = SphericalRefraction(100, -0.03, 1, 1.5, 100)
plane1 = OutputPlane(250)


ray00 = Ray([0,0,0],[0,0,100]) #the optial axis
ray01 = Ray([0,0,0],[4,0,100])
ray02 = Ray([0,0,0],[3,0,100])
ray03 = Ray([0,0,0],[2,0,100])
ray04 = Ray([0,0,0],[1,0,100])
ray05 = Ray([0,0,0],[-1,0,100])
ray06 = Ray([0,0,0],[-2,0,100])
ray07 = Ray([0,0,0],[-3,0,100])
ray08 = Ray([0,0,0],[-4,0,100])

sphere1.propagate_ray(ray00)
plane1.propagate_ray(ray00)
sphere1.propagate_ray(ray01)
plane1.propagate_ray(ray01)
sphere1.propagate_ray(ray02)
plane1.propagate_ray(ray02)
sphere1.propagate_ray(ray03)
plane1.propagate_ray(ray03)
sphere1.propagate_ray(ray04)
plane1.propagate_ray(ray04)
sphere1.propagate_ray(ray05)
plane1.propagate_ray(ray05)
sphere1.propagate_ray(ray06)
plane1.propagate_ray(ray06)
sphere1.propagate_ray(ray07)
plane1.propagate_ray(ray07)
sphere1.propagate_ray(ray08)
plane1.propagate_ray(ray08)

fig,ax = plt.subplots()
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.title('single spherical refracting surface(negative curvature)')
ray00.plot0(ax, color = 'blue')
ray01.plot0(ax, color = 'orange')
ray02.plot0(ax, color = 'plum')
ray03.plot0(ax, color = 'green')
ray04.plot0(ax, color = 'red')
ray05.plot0(ax, color = 'brown')
ray06.plot0(ax, color = 'pink')
ray07.plot0(ax, color = 'olive')
ray08.plot0(ax, color = 'gold')
plane0.plot0()