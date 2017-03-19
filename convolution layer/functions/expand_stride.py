import numpy as np

# recover the array from stride larger than 1 to stride 1

def expand_stride(self,sensitive_array):

    depth = sensitive_array.shape[0]
    expand_width = self.input_width - self.filter_width + 2*self.zero_padding +1
    expand_height = self.input_height - self.filter_height + 2*self.zero_padding +1
    expand_array = np.zeros((depth,expand_width,expand_height))

    for i in range(self.output_height):
        for j in range(self.output_width):

            # the new coordinate in the expand array
            i_pos = i *self.stride-1
            j_pos = j *self.stride-1
            expand_array[:,i_pos,j_pos]= sensitive_array[:,i,j]

    return expand_array

            

    
