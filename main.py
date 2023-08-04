import machine
from machine import ADC

# based on https://peppe8o.com/pulse-sensor-with-raspberry-pi-pico-hearth-beat-chech-with-micropython/
# setup the Pulse Sensor reading pin
pulse = ADC(28)
file = open("Pressed.txt", "w")
x = 0

# main program
while x < 20000:
    
    x = x + 1
    
    print("Running stuff")
    
    try:
        value=pulse.read_u16()
        file.write(str(value)+"\n")
        
    except OSError as e:
        machine.reset()