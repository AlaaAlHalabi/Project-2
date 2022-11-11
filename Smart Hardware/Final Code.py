import base64
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import RPi.GPIO as GPIO
import time
from io import BytesIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 26
GPIO_ECHO= 21
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
x=[ ]
y=[ ]
o=0.0     
for i in range(0,7):
    print ("Measured Distanceoo = %.1f cm" % o)
    m=0.0
    q=0.0
    GPIO.output(GPIO_TRIGGER, True)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)

    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival

    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2
    print ("Measured Distance1 = %.1f cm" % distance)
    
    m=(math.cos(math.radians(o))) * distance
    m1= round (m , 1)
    q=(math.sin(math.radians(o))) * distance
    q1= round (q , 1)
    print ("Measured Distancemm = %.1f cm" % m)
    print ("Measured Distanceqq = %.1f cm" % q)
    if (o <= 90) :
            x.append(m1)
            y.append(q1)
    if (o > 90 and o <= 180  ) :
             x.append(m1)
             y.append(q1)
             
    if (o > 180 and o <= 270  ) :
             x.append(m1)
             y.append(q1)
             
            
    if (o > 270  and o <= 360 ) :
             x.append(m1)
             y.append(q1)       
   
    print (x)      
    o=o+30       
    time.sleep(5)
    
    
    
  
  
  

#encode the figure
fig = plt.figure()
plt.plot(x, y,'k--' ) 
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.xlim(-200,200)
plt.ylim(-200,200)
plt.grid()
plt.show()

temp = BytesIO()
fig.savefig(temp,format='png')

fig_encode_bs64 = base64.b64encode(temp.getvalue()).decode('utf-8')

html_string = """
<center><h2>ULTRASONIC SENSOR</h2>
<img src = 'data:image/png;base64,{}'/>
""".format(fig_encode_bs64)

with open('/var/www/html/test.html', "w") as f:

    f.write(html_string)
