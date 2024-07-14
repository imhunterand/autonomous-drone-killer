import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

def send_data(x, y, fire):
    ser.write(f"{x},{y},{fire}\n".encode())

def close_connection():
    ser.close()
