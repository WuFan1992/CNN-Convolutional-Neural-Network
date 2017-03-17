import numpy as np

def calculate_output_size(input_size,filter_size,zero_padding,stride):
    return (input_size - filter_size + 2*zero_padding)/stride +1



def conv_2d(input_array,kernel_array,output_array,stride,zero_padding,bias):
    
    input_array_size=input_array.shape[0]
    kernel_array_size=kernel_array.shape[0]
    
    output_array_size=calculate_output_size(input_array_size,kernel_array_size,zero_padding,stride)
    for i in range(output_array_size):
        for j in range(output_array_size):
            output_array[i][j]=np.sum(input_array[i+kernel_array_size:j+kernel_array_size]*kernel)+bias
    
            
    
