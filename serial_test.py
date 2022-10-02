import serial

serial_path = "/dev/cu.usbmodem14101"

ser = serial.Serial(serial_path)

while True:
  if ser.isOpen():
    dat = ser.readline().strip().decode("utf-8")
    
    print(dat)