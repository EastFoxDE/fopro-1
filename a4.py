#### NOCH NICHTS GEÄNDERT
#### STAND VON a4!
import matplotlib.pyplot as plt
import numpy as np
from diffType import *
import math
import random

def sim(v0,angle,target):
    u = 2.0 * math.pi * angle / 360.0 
    d_y0 = v0 * u.sin() 
    d_x0 = v0 * u.cos() 
    
    # const
    g = 9.81
    t = 0.0 

    # Manthon Optimierung
    t = 2.0 / g * d_y0
    x = d_x0 * t
    return (target-x)**2

def minimize(v0,ang0,step):
    velo = diffType(v0)
    angle = diffType(ang0)

    eps = 1E-7
    step = 0.001
    count = 0
    
    while(1): 
        count += 1
    
        # Diff after velocity
        velo.dvalue = 1.0
        angle.dvalue = 0.0
        fx = sim(velo, angle,target)
        velo_dval = fx.dvalue
    
        # Diff after angle
        velo.dvalue = 0.0
        angle.dvalue = 1.0
        fx = sim(velo, angle,target)
        angle_dval = fx.dvalue
    
        #Debug
        #if(count % 100):
        #    pass #print(fx.value)
    
        if(fx.value < eps):
            break
    
        # Gradient descent
        velo = velo - step * velo_dval
        angle = angle - step * angle_dval
        
    #\x1b[31m\"red\"\x1b[0m"
    
    
    print(f"To land after exact \x1b[32m{target:.2f}\x1b[0m meter the velocity must be \x1b[31m{velo.value:.3f}\x1b[0m m/s with an angle of \x1b[31m{angle.value:.2f}\x1b[0m degrees.")
    print(f"The start values were: velocity = {v0:.2f}m/s | angle = {ang0:.2f} deg")
    print(f"Gradient count was: {count}")
    print("")
    
### init

random.seed()
for i in range(0,10):
    velo = random.uniform(5.0,50.0)
    angle = random.uniform(0.0,90.0)
    target = random.uniform(20.0,100.0) #20.0
    
    minimize(velo,angle,target)

