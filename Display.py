import serial
import time

#setup the serial port
ser=serial.Serial('/dev/ttyACM0',9600)

#encode the value and send it to arduino
def showVal(value): 
    resVal =str(value) + "ohms\n"
    resVal = resVal.encode()
    ser.write(resVal)
    time.sleep(1)


#encode waiting signal and send to arduino
def showWait():
    waitSig = "Waiting\n"
    waitSig = waitSig.encode()
    ser.write(waitSig)
    time.sleep(1)
