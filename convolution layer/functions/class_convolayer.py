import numpy as np
import conv_2d
import class_filter

# define the class of ConvoLayer

class ConvoLayer(object):

    def _init_(self, input_width,input_height,input_depth,filter_height,filter_width,filter_number,zero_padding,stride,learning_rate,activators):

        '''
        ConvoLayer has 3 parts:
            1. input array  ----- height width depth
            2. filter       ----- height width depth(the same as input array),number
            3. output array ----- height width depth (the same as filter number)


        we also need to combine the N filter together to forme a total filter
            
        '''

        # parameters input array
        self.input_height = input_height
        self.input_width = input_width
        self.input_depth = input_depth

        # parameters filter
        self.filter_height = filter_height
        self.filter_width = filter_width
        self.filter_depth =  input_depth
        self.filter_number = filter_number


        # parameters output
        self.output_height = calculate_output_size(input_height, filter_height,zero_padding,stride)
        self.output_width = calculate_output_size(input_width, filter_width,zero_padding,stride)
        self.output_depth = filter_number

        #other parameters
        self.zero_padding = zero_padding
        self.stride = stride
        self.activators = activators
        self.learning_rate = learning_rate

        # make up of filter
        self.filter_total = []
        for i in range(filter_number):
            filter_total.append(Filter(filter_height,filter_width,filter_depth))

        
            
        

        

        
