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
ax = fig.add_subplot (111, projection='3d'))
	TRIG = 16
    ECHO = 13
    TRIG1= 20
    ECHO1= 19
    TRIG2 = 21
    ECHO2 = 26
	x1=0
	x2=0
	x3=0
	z1=0
	z2=0
	z3=0
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
	ax.set_xlim(0 , 1000)
	ax.set_ylim(0 , 1000)
	ax.set_zlim(0 , 1000)

 for i in range (0,30):
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
     GPIO.output(TRIG1, False)
     time.sleep(2)
     GPIO.output(TRIG1, True)
     time.sleep(0.00001)
     GPIO.output(TRIG1, False)
     print ("Reading Sensor 2")
     while GPIO.input(ECHO1)==0:
     StartTime = time.time()
     while GPIO.input(ECHO1)==1:
     StopTime = time.time()   
     TimeElapsed = StopTime - StartTime
     distanc2 = (TimeElapsed * 34300) / 2
     GPIO.output(TRIG2, False) 
     time.sleep(2)
     GPIO.output(TRIG2, True)
     time.sleep(0.00001)
     GPIO.output(TRIG2, False)
     print ("Reading Sensor 3")
     while GPIO.input(ECHO2)==0:
     StartTime = time.time()
     while GPIO.input(ECHO2)==1:
     StopTime = time.time()   
     TimeElapsed = StopTime - StartTime
     distanc3 = (TimeElapsed * 34300) / 2
	 x1=x1+1
     y1=distanc1
	 z1=z1+1
	 x2=x2+1
	 y2=distanc2
	 z2=z2+1
	 x3=x3+1
	y3=distanc3
	z3=z3+1
	ax.scatter (x1,y1, z1 ,c='g', marker='o', linewidth=0.05)
	ax.scatter(x2,y2, z2 ,c='r', marker='o', linewidth=0.05)
	ax.scatter(x3,y3, z3 ,c='b', marker='o', linewidth=0.05)
	
	#encode the figure
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
