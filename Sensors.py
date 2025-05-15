from gpiozero import LineSensor

sensorL = LineSensor(4)
sensorR = LineSensor(5)
sensorC = LineSensor(6)

while True:
    if sensorL.value == 1:
        print("Line left detected")
    elif sensorR.value == 1:
        print("Line right detected")
    elif sensorC.value == 1:
        print("Line in center detected")
    else:
        print("No line detected")
