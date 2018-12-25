import serial

ser = 0

#Function to Initialize the Serial Port
def init_serial():
    COMNUM = 4          #Enter Your COM Port Number Here.
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = "COM4"   #COM Port Name Start from 0
    
    # ser.port = '/dev/ttyUSB0' #If Using Linux

    ser.timeout = 10
    ser.open()          #Opens SerialPort

    if ser.isOpen():
        print 'Open: ' + ser.portstr
        

init_serial()

temp = raw_input('Type what you want to send, hit enter:\r\n')
ser.write(temp)         #Writes to the SerialPort

while 1:    
    bytes = ser.readline()  #Read from Serial Port
    print 'You sent: ' + bytes      #Print What is Read from Port
    
#Ctrl+C to Close Python Window