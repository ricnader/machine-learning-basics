import numpy as np
import matplotlib as plt


def load_house_data():
    data = np.loadtxt("./data/houses.txt", delimiter=',', skiprows=1)
    X = data[:,:4]
    y = data[:,4]
    return X, y


def get_yhat(x,w,b):
  yhat = w*x+b
  return yhat

def get_gradients(x,yhat,w,b):  
  m =  x.shape
  
  
  for i in range(len(w)):
    for i in range(len(x)):
      d_dw = get_yhat(x,w,b) - y
    
      
    
    
  
  
  
