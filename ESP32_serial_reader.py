import serial


def main():
    port = 'COM3'  # Change as needed
    baudrate = 115200
    timeout = 3
    ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"Received: {line}") 
    
if __name__ == "__main__":
    main()