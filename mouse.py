#from pynput.mouse import Button,Controller
from pynput import mouse
#import mouse
import serial
ar=serial.Serial("COM3",9600)
def mous(x,y,button,pressed):
    if (button==mouse.Button.left  ):
        x=1
        cc=('X{:d}').format(x)
        ar.write(cc.encode())
        print("left clicked")


        #print("{} at {}".format('left'if pressed else 'releade',(x,y)))
    elif button==mouse.Button.right:
        c=0
        v=('Y{:d}').format(c)
        ar.write(v.encode())
        print("right clicked")

with mouse.Listener(on_click=mous) as listener:
    listener.join()


