import numpy as np
import expand_stride
import zero_padding
import class_convolayer
import class_filter
import conv_2d
import forward


# the main function of backward of convolution layer

def bp_sensitive_map(self,sensitive_map,activator):

    '''
    this function has 3 main steps
    1. recover the output sensitive map from stride larger than 1 to stride equals 1

    2. zero_padding

    3. calcul the convolution in order to get the sensitive map of layer i-1 


    '''
    # recover the output sensitive map to stride 1

    expand_array = expand_stride(sensitive_map)

    # zero_padding
    zp = (self.output_width - self.input_width + self.filter_width -1)/2

    padding_array = zero_padding(self.output_array,zp)

    # convolution
    deltat_sensitive = np.zeros((self.input_depth,self.filter_width,self.filter_height))
    

    for f in range(self.filter_number):
        filters = self.filter[f]
        
        deltat_each_filter = np.zeros((self.input_depth,self.filter_width,self.filter_height))
        for d in range(self.input_depth):
            conv_2d(sensitive_map[f],filters[d],deltat_each_filter[d],1,zp,self.bias)

        deltat_sensitive += deltat_each_filter

        
    derivate_array = np.array(self.input_array)
    treat_element(derivate_array,self.activator.Relu_backward)
    derivate_array *=deltat_sensitive



    
            
            
    
