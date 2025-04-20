import numpy as np 
import matplotlib.pyplot as pt 
import scipy.stats as stats
age = np.random.normal(2.5,2,1000)
average_speed = np.random.normal(90,5 ,1000)

slope, intercept  = stats.linregress(age,average_speed)

def predict_avg_speed(x):
    return x*slope + intercept

prediction_line = list(map(predict_avg_speed,age))

pt.scatter(age,average_speed)
pt.plot(age,prediction_line)
pt.show()