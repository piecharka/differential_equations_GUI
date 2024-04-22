import matplotlib.pyplot as plt
import numpy as np

def euler(f, a_endpoint, b_endpoint, N, initial_value, text_input):
  domain = np.zeros(N+1)
  result = np.zeros(N+1)
  h = (b_endpoint - a_endpoint) / N
  t = a_endpoint
  w = initial_value
  domain[0] = t
  result[0] = w

  for i in range(1,N+1):
    w = w + h*f(t,w, text_input)
    t = a_endpoint + i*h

    domain[i] = t
    result[i] = w
  
  return domain, result


def midpoint(f, a_endpoint, b_endpoint, N, initial_value, text_input):
  domain = np.zeros(N+1)
  result = np.zeros(N+1)
  h = (b_endpoint - a_endpoint)/N;
  t = a_endpoint
  w = initial_value
  domain[0] = t
  result[0] = w

  for i in range(1,N+1):
    w = w + h*f(t + h/2,w + h*f(t,w, text_input)/2, text_input)
    t = round(t + h,2)
    
    domain[i] = t
    result[i] = w
  return domain, result


def display(x, y, actual_values):
  plt.plot(x,y)
  plt.plot(x, actual_values)
  plt.show()


def display_multiple_plots(x_arr, y_arr, legend, actual_values):
  for i in range(len(x_arr)):
    plt.plot(x_arr[i],y_arr[i])
    plt.plot(x_arr[i], actual_values)
  plt.show()