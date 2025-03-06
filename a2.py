from diffType import *

#start
def gradient(x):
    g = 0.01             #stepsize
    p = diffType(x, 1.0) #our var to diff
    eps = 1e-7           #to stop diff
    count = 0            #for reference
    
    while(1):
        count += 1
        df_p = ((p**3)+(1 + p**2).sqrt())**2
        if(abs(df_p.dvalue) < eps):
            break
        p = p - g * df_p

    print("Found a minimum at x-cord: ",p.value, " on iteration ",count)
    
gradient(-0.5)
gradient(0)
gradient(-0.25)
