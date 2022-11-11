import base64
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from io import BytesIO
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
fig = plt.figure (figsize= (16,12))
ax = fig.add_subplot (111, projection='3d')
TRIG = 16
ECHO = 13
x1=0
z1=0
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
ax.set_xlim(0 , 100)
ax.set_ylim(0 , 1500)
ax.set_zlim(0 , 100)
def distance1():
    GPIO.output(TRIG, False)   
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    StartTime = time.time()
    StopTime = time.time()
    print ("Reading Sensor 1")
    while GPIO.input(ECHO)==0:
    StartTime = time.time()
    while GPIO.input(ECHO)==1:
    StopTime = time.time()   
    TimeElapsed = StopTime - StartTime
    distanc1 = (TimeElapsed * 34300) / 2
	return distanc1
if __name__ == '__main__':
 
   try:
 
       while True:
           dist1 = distance1()
           x1=x1+1
           y1=distanc1
           z1=z1+1
	   ax.scatter (x1,y1, z1 ,c='g', marker='o', linewidth=0.05)
   except KeyboardInterrupt:

        print("Measurement stopped by User")
   temp = BytesIO()
   fig.savefig(temp, format="jpg")
   fig_encode_bs64 = base64.b64encode(temp.getvalue()).decode('utf-8')
   html_string = """
   <center><h1>room layout</h1>
   <img src = 'data:image/png;base64,{}'/>
   """.format(fig_encode_bs64)
   with open('/var/www/html/test.html', "w") as f:
       f.write(html_string)
   plt.show()
       