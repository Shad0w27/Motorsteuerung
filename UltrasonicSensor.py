from gpiozero import DistanceSensor, LED

redLed = LED(1)
distanceSensor = DistanceSensor(10, 11, max_distance=1)

while True:
    if distanceSensor.distance <= 0.04:
        redLed.on()
    else:
        redLed.off()