import numpy as np
import class_convolayer
import class_filter

# zero_padding is used to add 0 in the surrouding of input array

def zero_padding(self,input_array,zp):
    '''
    zp is the number of 0 which we want to add in each side of each line

    there are 3 conditions we need to consider about
    1. no need to add 0 return original array
    2. 2-dimension:
    3. 3-dimension
     
   '''

    if zp == 0:
        return input_array
    else:
        if input_array.ndim == 3:
            input_height = input_array.shape[2]
            input_width = input_array.shape[1]
            input_depth = input_array.shape[0]

            expand_array = np.zeros((input_depth,input_height+2*zp,input_weight+2*zp))
            expand_array[:,zp:zp+input_height,zp:zp+input_weight] = input_array
            return expand_array


            else:
                if input_array.ndim == 2:
                    input_height = input_array.shape[1]
                    input_width = input_array.shape[0]

                    expand_array = np.zeros((input_height+2*zp,input_width+2*zp))
                    expand_array = [zp:zp+input_height,zp:zp+input_width] = input_array
                    return expand_array
                    
                





    
    

    
            
        
        
    
