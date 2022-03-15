# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:54:32 2022

@author: Shekhar Rajput
"""

import numpy as np
import pickle


loaded_model = pickle.load(open('model.sav','rb'))
input_data =(1,2,3,4,5,6,7)
numpy_array = np.asarray(input_data)
input =numpy_array.reshape(1,-1)
prediction = loaded_model.predict(input)
print(prediction)