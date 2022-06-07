#Script Begins
# importing modules
import numpy as np
import matplotlib.pyplot as plt
  
# creating dataset
data = [4,12,32,46,53,59,60 ]
  
# creating class interval
classInterval = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,100,110,120,130,140,150,160,170]
  
# calculating frequency and class interval
values, base = np.histogram(data, bins=classInterval)
  
# calculating cumulative sum
cumsum = np.cumsum(values)
  
# plotting  the ogive graph
plt.plot(base[1:], cumsum, color='red', marker='o', linestyle='-')
  
# formatting
plt.title('Ogive Graph')
#Script ends
plt.xlabel('Marks in End-Term')
plt.ylabel('Cumulative Frequency')