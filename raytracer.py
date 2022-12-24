# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#%%
'''
This module contains several classes for 2nd year Physics Project A: An Optical Ray Tracer
    
    Ray                         Class represents optical rays in terms of position and direction 
                                with 3-element NumPy arrays.
    
    OpticalElement              A base class that contains derived classes- SphericalRefraction
                                and OutputPlane. 
    
    SphericalRefraction         Derived class from OpticalElement; if the optical ray intersects 
                                the spherical refracting surface the class refracts and propagates 
                                the ray                          
    
    OutputPlane                 Derived class from OpticalElement; it propagates the optical ray
                                to a plane in x-y where the ray terminates       
'''
#%%

class Ray:
    '''
    Ray class represents optical light ray.
    
    '''
    def __init__(self, p = [0, 0, 0], k = [0, 0, 1]):
        '''
        Contains all necessary attributes for the class.
        
        Parameters
        ----------
        p : list
            starting position vector of the ray, the default is [0, 0, 0]
        k : list
            starting direction vector of the ray, the default is [0, 0, 1]

        Raises
        ------
        Exception
            to ensure the p and k input alway have the corerect dimension

        '''
        if len(p) != 3:
            raise Exception("Ray parameter has incorrect size") 
       
        self.position = [p]
        
        self.direction = [k]
       
    def __repr__(self):
        '''
        String representation of the ray object.
        '''
        return "%s(r=array(%r), d=array(%r))" % ("Ray", self.position, self.direction)
   
    def append(self, p, k):
        '''
        Appending values of p and k to the ray object.
        '''
        self.position.append(p)
        self.direction.append(k)
       
    def k(self):
        '''
        The current dirction of the ray.
        '''
        return self.direction[-1] #returns the last index of the list, i.e. the current direction
   
    def p(self):
        '''
        The current position of the ray.
        '''
        return self.position[-1] #returns the last index of the list, i.e. the current position
   
    def vertices(self):
        '''
        An array of all points along the ray's trajectory.
        '''
        self.position = np.array(self.position)
        return self.position
 
    def plot0(self, ax, color):
        '''
        Plots the z and x vertices of the ray.
        '''
        ax.plot(self.vertices()[:, 2], self.vertices()[:, 0], color = color)

#%%
#Snell's Law function   
def refraction2(N, k1_hat, n1, n2):
    '''
    Using the vector form te Snell's law to determine the direction of the refracted ray, k2_hat.
     
    Derivation from StarkEffects.com: http://www.starkeffects.com/snells-law-vector.shtml 
    
    Parameters
    ----------
    N : array of int
        normalised normal vector
    k1_hat : array of int
        normalised incident ray vector
    n1 : float
        refracive index on the incident ray side
    n2 : float
        refracive index on the refracted ray side

    Returns
    -------
    k2_hat : array of int
        normalised refracted ray vector

    '''
    theta1 = np.arccos(np.dot(k1_hat, N))
    N =np.array(N)
    k1_hat = np.array(k1_hat)
    k2_hat = (n1/n2) * (np.cross(N, np.cross(-N, k1_hat))) - (N * np.sqrt(1 - (n1/n2)**2 * (np.dot(np.cross(N, k1_hat), np.cross(N, k1_hat)))))
    if np.sin(theta1) < n2/n1:
        return k2_hat
    else: 
        return None
#%%

class OpticalElement:
    '''
    All optical element will inherit this base class, and will have to implement the propagate_ray method somehow.
    '''
    def propagate_ray(self, ray):
        "propagate a ray through the optical element"
        raise NotImplementedError()

    

class SphericalRefraction(OpticalElement):
    '''
    A drived classed from OpticalElement.
    '''
    def __init__(self, z0, cur, n1, n2, ar):
        '''
        Contains all necessary attributes for the class.
    
        Parameters
        ----------
        z0 : float
            the z coordinate of where the ray intercepts the spherical refracting surface
        cur : float
            curvature of the spherical refracting surface
        n1 : pfoat
            refracive index on the incident ray side
        n2 : float
            refracive index on the refracted ray side
        ar : int
            aperture radius

        '''
        
        self._intercept_z = z0
        
        self._curvature = cur
        
        self._refractive_index_1 = n1
        
        self._refractive_index_2 = n2
        
        self._aperture_radius = ar
        #initialising the five parameters for refracting at surfaces
        
        self._radius_of_curvature = 1/cur
        
        self.centre = np.array([0, 0, self._intercept_z + self._radius_of_curvature])
            
        self.first_int = np.array([0, 0, 0])
        
    def intercept(self, ray):
        '''
        Determines the first real intercept betwen the optical ray and the spherical surface
        '''
       
        k_hat = ray.k()/np.linalg.norm(ray.k())
        
        
        self.vec_r = np.array([ray.p()[0] - self.centre[0], ray.p()[1] - self.centre[1], ray.p()[2] - self.centre[2]])
        mod_vec_r = np.sqrt( self.vec_r[0]**2 +  self.vec_r[1]**2 +  self.vec_r[2]**2)
        l1 = np.dot(- self.vec_r, k_hat) + np.sqrt(np.dot( self.vec_r, k_hat)**2 - (mod_vec_r**2 - self._radius_of_curvature**2))
        l2 = np.dot(- self.vec_r, k_hat) - np.sqrt(np.dot( self.vec_r, k_hat)**2 - (mod_vec_r**2 - self._radius_of_curvature**2))
        minimum = np.minimum(l1,l2)
        self.first_int = minimum * k_hat + ray.p()
        discriminant = np.dot( self.vec_r, k_hat)**2 - (mod_vec_r**2 - self._radius_of_curvature**2)
        if discriminant > 0:
            return self.first_int
        elif discriminant <=0:
            return None
        

    def propagate_ray(self, ray):
        '''
        Propagates an optical ray thorugh the optical element, done in tree steps:
            finding the intercept
            finding the normalised refrated direction vectore
            append the latest position and direction
        '''
        if self._curvature != 0:
            N = np.subtract(self.intercept(ray), self.centre)
            N_hat = N/np.linalg.norm(N)
            k1_hat = ray.k()/np.linalg.norm(ray.k())
            k2_hat = refraction2(N_hat, k1_hat, self._refractive_index_1, self._refractive_index_2)
            ray.append(self.intercept(ray), k2_hat)
            return (ray.p(), ray.k())
        elif self._curvature == 0:
            N_hat = [0, 0, 1]
            k1_hat = ray.k()/np.linalg.norm(ray.k())
            k2_hat = refraction2(N_hat, k1_hat, self._refractive_index_1, self._refractive_index_2)
            ray.append(self.intercept(ray), k2_hat)
            return (ray.p(), ray.k())
     
    def plot0(self,ax):
        '''
        plots the spherical refracting surface.
        '''
        ax.add_patch(plt.Circle((self.centre[2], self.centre[0]), 1/self._curvature, edgecolor='grey', fill=False))


class OutputPlane(OpticalElement):
    '''
    A derived classed from OpticalElement, a plane where the propagation of the ray terminates
    '''
    def __init__(self, i_out):
        '''
        Parameters
        ----------
        i_out : int
            the z coordinate of where the output plane is placed
        '''
        self.output_int = i_out
        
    def intercept_out(self, ray):
        '''
        Position vector where the optical ray intercpets the output plane
        '''
        p_out =ray.p()
        k_out = ray.k() #new direction
        l_out = np.subtract(self.output_int, p_out[2])
        return np.add(p_out, np.multiply(l_out, k_out))
    
    def propagate_ray(self, ray):
        '''
        Propagates the ray to the output plane and appending its position to the vertices
        '''
        point_out = self.intercept_out(ray)
        ray.append(point_out, ray.k())
    
    def plot0(self):
        '''
        Plots the output plane at a given z value
        '''
        plt.axvline(self.output_int, color = 'grey')


