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
def distance():
    # set Trigger to HIGH

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
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
			      
            x1=x1+1
            y1=dist
            z1=z1+1
	        ax.scatter (x1,y1, z1 ,c='g', marker='o', linewidth=0.05) 

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
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
       