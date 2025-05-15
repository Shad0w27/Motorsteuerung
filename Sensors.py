from gpiozero import LineSensor, DigitalOutputDevice

sensorEnable = DigitalOutputDevice(17)
sensorL = LineSensor(4)
sensorR = LineSensor(5)
sensorC = LineSensor(6)

sensorEnable.on()
for i in range(50):
    if sensorL.value == 1:
        print("Line left detected")
    elif sensorR.value == 1:
        print("Line right detected")
    elif sensorC.value == 1:
        print("Line in center detected")
    else:
        print("No line detected")

sensorEnable.off()