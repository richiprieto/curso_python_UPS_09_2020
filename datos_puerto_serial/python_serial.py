# pip3 install pyserial
import serial

ser = serial.Serial("/dev/ttyACM0")
print("Solicitando datos:")
ser.write(b"enviar")
while True:
    line = ser.readline()
    try:
        print(str(int(line)))
    except:
        break
print("Trama completa recibida")
ser.close()
