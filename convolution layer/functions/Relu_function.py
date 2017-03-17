import numpy as np
import class_convolayer

# this class is used to calcul the forward and the backward of Relu function

class Relu(object):

    # forward function
    def Relu_forward(self,z):
        return max(0,z)


    # backward function
    def Relu_backward(self,output):
        return 1 if output > 0 else 0

