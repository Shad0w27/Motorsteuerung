from gpiozero import LineSensor, DigitalOutputDevice, Motor, PWMOutputDevice

sensorEnable = DigitalOutputDevice(2)
sensorL = LineSensor(14)
sensorR = LineSensor(18)
sensorC = LineSensor(15)

EmL = PWMOutputDevice(22)
EmR = PWMOutputDevice(27)
motorL = Motor(forward=18, backward=23)
motorR = Motor(forward=24, backward=25)

sensorEnable.on()

for i in range(50):
    print(f"L: {sensorL.value}, R: {sensorR.value}, C: {sensorC.value}")
    if sensorL.value == 1:
        motorL.forward()
        motorR.stop()
    elif sensorR.value == 1:
        motorR.forward()
        motorL.stop()
    elif sensorC.value == 1:
        motorL.forward()
        motorR.forward()
    else:
        motorL.stop()
        motorR.stop()

sensorEnable.off()
sensorL.close()
sensorR.close()
sensorC.close()
motorL.close()
motorR.close()
sensorEnable.close()