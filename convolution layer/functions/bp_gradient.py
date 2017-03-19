import numpy as np
import bp_sensitive_map



# update the weight and the bias

def bp_gradient(self,sensitive_map):

    expand_array = expand_stride(sensitive_map)

    for i in range(self.filter_number):
        for d in range(filter.weights.shape[0]):
                conv(self.padded_input_array[d], 
                     expanded_array[f],
                     filter.weights_grad[d], 1, 0)
            filter.bias_grad = expanded_array[f].sum()
