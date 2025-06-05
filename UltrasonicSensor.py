from gpiozero import DistanceSensor
from time import sleep

distanceSensor = DistanceSensor(23, 24)  # Trigger pin 23, Echo pin 24

while True:
    print("Distance: ", distanceSensor.distance * 100, "cm")
    sleep(1)  # Delay for 1 second before the next reading